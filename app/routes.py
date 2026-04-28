from fastapi import APIRouter
from app.analytics import calculate_metrics

router = APIRouter()

@router.get("/metrics")
def get_metrics():
    data = {
        "clicks": 1200,
        "signups": 150,
        "deposits": 45
    }
    return calculate_metrics(data)
