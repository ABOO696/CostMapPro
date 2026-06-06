from collections import defaultdict

from app.services.finmind_client import (
    FinMindClient
)

from app.database.models.institutional import (
    InstitutionalBuySell
)

def sync_institution(
    db,
    stock_id,
    start_date
):

    client = FinMindClient()

    rows = client.get(
        dataset=
        "TaiwanStockInstitutionalInvestorsBuySell",
        data_id=stock_id,
        start_date=start_date
    )

    daily = defaultdict(
        lambda: {
            "foreign":0,
            "trust":0,
            "dealer":0
        }
    )

    for row in rows:

        d = row["date"]

        net_buy = (
            row["buy"]
            -
            row["sell"]
        )

        name = row["name"]

        if "Foreign" in name:

            daily[d]["foreign"] += net_buy

        elif "Investment Trust" in name:

            daily[d]["trust"] += net_buy

        elif "Dealer" in name:

            daily[d]["dealer"] += net_buy

    for trade_date, value in daily.items():

        db.merge(

            InstitutionalBuySell(

                stock_id=stock_id,

                trade_date=trade_date,

                foreign_investor=
                value["foreign"],

                investment_trust=
                value["trust"],

                dealer=
                value["dealer"],

                total_net_buy=
                value["foreign"]
                +
                value["trust"]
                +
                value["dealer"]
            )
        )

    db.commit()