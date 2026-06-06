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


class InstitutionPosition(Base):

    __tablename__ = "institution_position"

    stock_id: Mapped[str] = mapped_column(
        String(10),
        primary_key=True
    )

    trade_date: Mapped[date] = mapped_column(
        Date,
        primary_key=True
    )

    foreign_position: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    foreign_cost: Mapped[float] = mapped_column(
        Numeric(10, 2),
        default=0
    )

    trust_position: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    trust_cost: Mapped[float] = mapped_column(
        Numeric(10, 2),
        default=0
    )

    dealer_position: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    dealer_cost: Mapped[float] = mapped_column(
        Numeric(10, 2),
        default=0
    )