import time
from typing import Dict, Any

def send_push_notification(target: Dict[str, Any], message: str) -> Dict[str, Any]:
    """
    Mock bildirim gönderimi.
    Gerçek sistemde Firebase/APNs entegre edilecektir.
    """
    # Demo gecikme simülasyonu (isteğe bağlı)
    time.sleep(0.05)

    return {
        "sent": True,
        "target_user_id": target.get("user_id"),
        "target_plate": target.get("plate"),
        "message": message,
        "provider": "mock"
    }
