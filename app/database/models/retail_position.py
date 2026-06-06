from datetime import date

from sqlalchemy import (
    String,
    Date,
    Numeric,
    BigInteger
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class RetailPosition(Base):

    __tablename__ = "retail_position"

    stock_id: Mapped[str] = mapped_column(
        String(10),
        primary_key=True
    )

    trade_date: Mapped[date] = mapped_column(
        Date,
        primary_key=True
    )

    margin_balance: Mapped[int] = mapped_column(
        BigInteger
    )

    retail_cost: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )