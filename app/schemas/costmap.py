from pydantic import BaseModel


class CostMapResponse(BaseModel):

    trade_date: str

    close_price: float

    major_cost: float

    retail_cost: float

    foreign_cost: float

    trust_cost: float

    dealer_cost: float

    cost_gap: float

    cost_score: float