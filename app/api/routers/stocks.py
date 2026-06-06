from fastapi import APIRouter

from app.database.session import SessionLocal

from app.database.models.stock_info import (
    StockInfo
)

router = APIRouter()


@router.get("/stocks")
def get_stocks():

    db = SessionLocal()

    rows = db.query(
        StockInfo
    ).all()

    result = []

    for row in rows:

        result.append({
            "stock_id":
            row.stock_id,

            "stock_name":
            row.stock_name,

            "industry_category":
            row.industry_category,

            "market":
            row.market
        })

    db.close()

    return result