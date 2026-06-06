from fastapi import APIRouter

from sqlalchemy import desc

from app.database.session import (
    SessionLocal
)

from app.database.models.cost_map_daily import (
    CostMapDaily
)

router = APIRouter()


@router.get("/radar")
def radar(limit: int = 50):

    db = SessionLocal()

    rows = (

        db.query(
            CostMapDaily
        )

        .order_by(
            desc(
                CostMapDaily.cost_score
            )
        )

        .limit(limit)

        .all()
    )

    result = []

    for row in rows:

        result.append({

            "stock_id":
            row.stock_id,

            "cost_score":
            float(
                row.cost_score
            ),

            "major_cost":
            float(
                row.major_cost
            ),

            "retail_cost":
            float(
                row.retail_cost
            ),

            "cost_gap":
            float(
                row.cost_gap
            )
        })

    db.close()

    return result