from app.services.finmind_client import (
    FinMindClient
)

from app.database.models.stock_info import (
    StockInfo
)

def sync_stock_info(db):

    client = FinMindClient()

    rows = client.get(
        dataset="TaiwanStockInfo"
    )

    for row in rows:

        db.merge(
            StockInfo(
                stock_id=row["stock_id"],
                stock_name=row["stock_name"],
                industry_category=row.get(
                    "industry_category"
                ),
                market=row.get("type")
            )
        )

    db.commit()

    print(
        f"stock_info synced {len(rows)}"
    )