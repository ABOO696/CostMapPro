from pydantic import BaseModel


class StockResponse(BaseModel):

    stock_id: str

    stock_name: str

    industry_category: str | None = None

    market: str | None = None

    class Config:
        from_attributes = True