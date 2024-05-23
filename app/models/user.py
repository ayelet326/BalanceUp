from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    password: str
    email: Optional[str]
    phone: Optional[str]
    current_balance: float
