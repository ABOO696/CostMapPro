from datetime import date

from sqlalchemy import (
    String,
    Date,
    BigInteger
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class MarginShort(Base):

    __tablename__ = "margin_short"

    stock_id: Mapped[str] = mapped_column(
        String(10),
        primary_key=True
    )

    trade_date: Mapped[date] = mapped_column(
        Date,
        primary_key=True
    )

    margin_balance: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    margin_change: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    short_balance: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    short_change: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )