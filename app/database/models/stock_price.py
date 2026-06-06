from datetime import date

from sqlalchemy import (
    String,
    Date,
    Numeric,
    BigInteger,
    Index
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class StockPrice(Base):

    __tablename__ = "stock_price"

    stock_id: Mapped[str] = mapped_column(
        String(10),
        primary_key=True
    )

    trade_date: Mapped[date] = mapped_column(
        Date,
        primary_key=True
    )

    open: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    high: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    low: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    close: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    volume: Mapped[int] = mapped_column(
        BigInteger
    )

    trading_money: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True
    )

    __table_args__ = (
        Index(
            "idx_price_stock_date",
            "stock_id",
            "trade_date"
        ),
    )