from datetime import date

from sqlalchemy import (
    String,
    Date,
    Numeric
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class CostMapDaily(Base):

    __tablename__ = "cost_map_daily"

    stock_id: Mapped[str] = mapped_column(
        String(10),
        primary_key=True
    )

    trade_date: Mapped[date] = mapped_column(
        Date,
        primary_key=True
    )

    major_cost: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    retail_cost: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    foreign_cost: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    trust_cost: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    dealer_cost: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    cost_gap: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    accumulation_score: Mapped[float] = mapped_column(
        Numeric(5, 2),
        default=0
    )

    momentum_score: Mapped[float] = mapped_column(
        Numeric(5, 2),
        default=0
    )

    cost_score: Mapped[float] = mapped_column(
        Numeric(5, 2),
        default=0
    )