from pydantic import BaseModel


class RadarResponse(BaseModel):

    stock_id: str

    cost_score: float

    major_cost: float

    retail_cost: float

    cost_gap: float

    class Config:
        from_attributes = True