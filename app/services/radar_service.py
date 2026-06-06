from sqlalchemy import desc

from app.database.models.cost_map_daily import (
    CostMapDaily
)


def top_radar(
    db,
    limit=50
):

    return (

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