from ..connection import get_database
from ...models.user import User
from bson import ObjectId

db = get_database()
users_collection = db["users"]


async def create_user(user: User):
    user_dict = user.dict()
    result = await users_collection.insert_one(user_dict)
    user.id = str(result.inserted_id)
    await users_collection.update_one({'_id': result.inserted_id}, {'$set': {'id': user.id}})
    return user


async def get_user_by_id(user_id: ObjectId) -> User:
    user_data = await users_collection.find_one({"_id": user_id})
    return User(**user_data) if user_data else None


async def update_user(user_id: ObjectId, user: User):
    await users_collection.update_one({"_id": user_id}, {"$set": user.dict()})


async def delete_user(user_id: ObjectId):
    await users_collection.delete_one({"_id": user_id})


async def find_user_by_credentials(username: str, password: str) -> User:
    user_data = await users_collection.find_one({"name": username, "password": password})
    return User(**user_data) if user_data else None
