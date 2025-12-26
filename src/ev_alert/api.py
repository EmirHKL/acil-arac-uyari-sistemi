import logging
from .notifications import send_push_notification
from .notifications import send_push_notification
from fastapi import FastAPI
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("ev-alert")
from pydantic import BaseModel
from .geo import haversine_m

app = FastAPI(title="Acil Durum Araçları Uyarı Sistemi API")

class LocationIn(BaseModel):
    vehicle_id: str
    lat: float
    lon: float

# Demo amaçlı: sistemde kayıtlı kullanıcı araçları
# Gerçekte bunlar PostgreSQL’den gelecektir.
REGISTERED_VEHICLES = [
    {"user_id": "U1", "plate": "33ABC001", "lat": 36.8000, "lon": 34.6200},
    {"user_id": "U2", "plate": "33ABC002", "lat": 36.8010, "lon": 34.6210},
    {"user_id": "U3", "plate": "33ABC003", "lat": 36.9000, "lon": 34.7000},
]

@app.get("/")
def root():
    return {"status": "ok", "message": "API çalışıyor"}

@app.post("/location")
def ingest_location(payload: LocationIn):
    # 100 metre menzil içinde kalanları bul
    targets = []
    for v in REGISTERED_VEHICLES:
        d = haversine_m(payload.lat, payload.lon, v["lat"], v["lon"])
        if d <= 100.0:
            targets.append({
                "user_id": v["user_id"],
                "plate": v["plate"],
                "distance_m": round(d, 2)
            })

    # Mock bildirim gönder (hedeflere)
    notification_results = []
    for t in targets:
        r = send_push_notification(
            user_id=t["user_id"],
            title="Acil Durum Aracı Uyarısı",
            body="Acil durum aracı yaklaşıyor, lütfen yolu açın.",
            data={"radius_m": 100, "vehicle_id": payload.vehicle_id}
        )
        notification_results.append({
            "user_id": t["user_id"],
            "success": r.success,
            "provider": r.provider,
            "message_id": r.message_id,
        })
            # Bildirimleri tetikle (mock)
    notif_results = []
    message = "Acil durum aracı yaklaşıyor, yolu açın."

    for t in targets:
        r = send_push_notification(t, message)
        notif_results.append(r)

    logger.info(
        "location_received vehicle_id=%s target_count=%s",
        payload.vehicle_id, len(targets)
    )

    return {
        "vehicle_id": payload.vehicle_id,
        "emergency_vehicle_location": {"lat": payload.lat, "lon": payload.lon},
        "radius_m": 100,
        "target_count": len(targets),
        "targets": targets,
        "notifications": notif_results
    }


    return {
        "vehicle_id": payload.vehicle_id,
        "emergency_vehicle_location": {"lat": payload.lat, "lon": payload.lon},
        "radius_m": 100,
        "target_count": len(targets),
        "targets": targets,
        "notifications": notification_results
    }
