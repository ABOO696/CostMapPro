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


class InstitutionalBuySell(Base):

    __tablename__ = "institutional_buy_sell"

    stock_id: Mapped[str] = mapped_column(
        String(10),
        primary_key=True
    )

    trade_date: Mapped[date] = mapped_column(
        Date,
        primary_key=True
    )

    foreign_investor: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    investment_trust: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    dealer: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    total_net_buy: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )