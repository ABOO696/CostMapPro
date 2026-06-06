from sqlalchemy import desc

from app.database.session import SessionLocal

from app.database.models.cost_map_daily import (
    CostMapDaily
)


class StockService:

    @staticmethod
    def radar(limit=50):

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

        db.close()

        return rows