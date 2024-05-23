from pydantic import BaseModel
from enum import Enum
from typing import Union
from datetime import date


class ExpenseCategory(str, Enum):
    Housing = "Housing"
    Utilities = "Utilities"
    Transportation = "Transportation"
    Food = "Food"
    Insurance = "Insurance"
    Debt = "Debt"
    Payments = "Payments"
    Entertainment = "Entertainment"
    Healthcare = "Healthcare"
    Education = "Education"
    Personal = "Personal"
    Care = "Care"
    Clothing = "Clothing"
    Savings = "Savings"
    Investments = "Investments"
    Gifts = "Gifts"
    Travel = "Travel"
    Childcare = "Childcare"
    Pets = "Pets"
    Taxes = "Taxes"
    Home = "Home"
    Maintenance = "Maintenance"
    Technology = "Technology"
    income = "income"
    expense = "expense"


class Expense(BaseModel):
    amount: float
    description: str
    date: date
    user_id: int
    category: Union[ExpenseCategory, str]
