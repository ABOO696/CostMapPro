from fastapi import APIRouter

from sqlalchemy import func

from app.database.session import (
    SessionLocal
)

from app.database.models.cost_map_daily import (
    CostMapDaily
)

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    db = SessionLocal()

    total = db.query(
        CostMapDaily.stock_id
    ).distinct().count()

    avg_score = db.query(
        func.avg(
            CostMapDaily.cost_score
        )
    ).scalar()

    bullish = db.query(
        CostMapDaily
    ).filter(
        CostMapDaily.cost_score >= 80
    ).count()

    db.close()

    return {

        "total_stock":
        total,

        "avg_score":
        round(
            avg_score or 0,
            2
        ),

        "bullish_count":
        bullish
    }