from datetime import date

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class StockInfo(Base):

    __tablename__ = "stock_info"

    stock_id: Mapped[str] = mapped_column(
        String(10),
        primary_key=True
    )

    stock_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    industry_category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    market: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    listing_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )