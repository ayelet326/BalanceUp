from ..connection import get_database
from ...models.user import User
from bson import ObjectId
from typing import List

db = get_database()
users_collection = db["users"]


def create_user(user: User) -> ObjectId:
    result = users_collection.insert_one(user.dict())
    return result.inserted_id


def get_user_by_id(user_id: ObjectId) -> User:
    user_data = users_collection.find_one({"_id": user_id})
    return User(**user_data) if user_data else None


def update_user(user_id: ObjectId, user: User):
    users_collection.update_one({"_id": user_id}, {"$set": user.dict()})


def delete_user(user_id: ObjectId):
    users_collection.delete_one({"_id": user_id})


# def get_all_users() -> List[User]:
#     user_data = users_collection.find({})
#     return [User(**user) for user in user_data]
