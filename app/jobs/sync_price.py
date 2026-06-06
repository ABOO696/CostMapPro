from app.services.finmind_client import (
    FinMindClient
)

from app.database.models.stock_price import (
    StockPrice
)

def sync_price(
    db,
    stock_id,
    start_date
):

    client = FinMindClient()

    rows = client.get(
        dataset="TaiwanStockPrice",
        data_id=stock_id,
        start_date=start_date
    )

    for row in rows:

        db.merge(

            StockPrice(

                stock_id=row["stock_id"],

                trade_date=row["date"],

                open=row["open"],

                high=row["max"],

                low=row["min"],

                close=row["close"],

                volume=row[
                    "Trading_Volume"
                ],

                trading_money=row[
                    "Trading_money"
                ]
            )
        )

    db.commit()

    print(
        stock_id,
        len(rows)
    )