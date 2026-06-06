from fastapi import APIRouter

from app.database.session import (
    SessionLocal
)

from app.database.models.cost_map_daily import (
    CostMapDaily
)

router = APIRouter()


@router.get(
    "/costmap/{stock_id}"
)
def get_costmap(
    stock_id: str
):

    db = SessionLocal()

    rows = (

        db.query(
            CostMapDaily
        )

        .filter(
            CostMapDaily.stock_id
            ==
            stock_id
        )

        .order_by(
            CostMapDaily.trade_date
        )

        .all()
    )

    result = []

    for row in rows:

        result.append({

            "trade_date":
            row.trade_date,

            "close_price":
            float(
                row.close_price
            ),

            "major_cost":
            float(
                row.major_cost
            ),

            "retail_cost":
            float(
                row.retail_cost
            ),

            "foreign_cost":
            float(
                row.foreign_cost
            ),

            "trust_cost":
            float(
                row.trust_cost
            ),

            "dealer_cost":
            float(
                row.dealer_cost
            ),

            "cost_gap":
            float(
                row.cost_gap
            ),

            "cost_score":
            float(
                row.cost_score
            )
        })

    db.close()

    return result