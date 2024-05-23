from typing import List

from ..connection import get_database
from ...models.income import Income
from bson import ObjectId

db = get_database()
incomes_collection = db["incomes"]


def create_income(income: Income) -> ObjectId:
    result = incomes_collection.insert_one(income.dict())
    return result.inserted_id


def get_income_by_id(income_id: ObjectId) -> Income:
    income_data = incomes_collection.find_one({"_id": income_id})
    return Income(**income_data) if income_data else None


def update_income(income_id: ObjectId, income: Income):
    incomes_collection.update_one({"_id": income_id}, {"$set": income.dict()})


def delete_income(income_id: ObjectId):
    incomes_collection.delete_one({"_id": income_id})


def get_incomes_by_user_id(user_id: ObjectId) -> List[Income]:
    income_data = incomes_collection.find({"user_id": user_id})
    return [Income(**income) for income in income_data]
