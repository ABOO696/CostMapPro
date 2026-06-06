from app.jobs.sync_price import (
    sync_price
)

from app.jobs.sync_margin import (
    sync_margin
)

from app.jobs.sync_institution import (
    sync_institution
)

def sync_one_stock(
    db,
    stock_id,
    start_date
):

    sync_price(
        db,
        stock_id,
        start_date
    )

    sync_institution(
        db,
        stock_id,
        start_date
    )

    sync_margin(
        db,
        stock_id,
        start_date
    )