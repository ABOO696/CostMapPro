from app.services.finmind_client import (
    FinMindClient
)

from app.database.models.margin_short import (
    MarginShort
)

def sync_margin(
    db,
    stock_id,
    start_date
):

    client = FinMindClient()

    rows = client.get(
        dataset=
        "TaiwanStockMarginPurchaseShortSale",
        data_id=stock_id,
        start_date=start_date
    )

    for row in rows:

        db.merge(

            MarginShort(

                stock_id=row["stock_id"],

                trade_date=row["date"],

                margin_balance=
                row[
                    "MarginPurchaseTodayBalance"
                ],

                margin_change=
                row[
                    "MarginPurchaseBuy"
                ]
                -
                row[
                    "MarginPurchaseSell"
                ],

                short_balance=
                row[
                    "ShortSaleTodayBalance"
                ],

                short_change=
                row[
                    "ShortSaleBuy"
                ]
                -
                row[
                    "ShortSaleSell"
                ]
            )
        )

    db.commit()