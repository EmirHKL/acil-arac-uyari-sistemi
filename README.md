# Acil Durum Araçları Uyarı Sistemi

![Proje Posteri](assets/poster.png)
## Çalıştırma
```powershell
uvicorn src.ev_alert.api:app --reload
curl -X POST http://127.0.0.1:8000/location `
-H "Content-Type: application/json" `
-d '{"vehicle_id":"AMB-001","lat":36.8,"lon":34.62}'
