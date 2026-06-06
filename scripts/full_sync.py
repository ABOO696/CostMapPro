from app.database.session import (
    SessionLocal
)

from app.database.models.stock_info import (
    StockInfo
)

from app.jobs.sync_one_stock import (
    sync_one_stock
)

db = SessionLocal()

stocks = (
    db.query(
        StockInfo
    )
    .all()
)

for stock in stocks:

    print(
        stock.stock_id
    )

    sync_one_stock(
        db,
        stock.stock_id,
        "2023-01-01"
    )

db.close()