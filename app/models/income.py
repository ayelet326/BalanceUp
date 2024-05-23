from pydantic import BaseModel
from datetime import date

class Income(BaseModel):
    amount: float
    source: str
    description: str
    date: date
    user_id: int
