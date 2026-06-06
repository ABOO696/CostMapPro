from apscheduler.schedulers.blocking import (
    BlockingScheduler
)

from app.database.session import (
    SessionLocal
)

from app.database.models.stock_info import (
    StockInfo
)

from app.jobs.sync_one_stock import (
    sync_one_stock
)

from app.utils.date_utils import (
    get_start_date
)

def run_daily():

    db = SessionLocal()

    start_date = get_start_date()

    stocks = (
        db.query(
            StockInfo
        )
        .all()
    )

    for stock in stocks:

        sync_one_stock(
            db,
            stock.stock_id,
            start_date
        )

    db.close()

scheduler = BlockingScheduler()

scheduler.add_job(
    run_daily,
    "cron",
    hour=20,
    minute=0
)

scheduler.start()