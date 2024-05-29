from typing import Optional
from bson import ObjectId
from fastapi import HTTPException

from ..db_manegement.repositories import user_repository as UserRepository
from ..models import user
from ..models.user import User


async def create_user(user_data: user):
    try:
        user_data.is_valid_user()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    # Call the repository to insert the user
    user_data = await UserRepository.create_user(user_data)
    return user_data


async def get_user_by_id(user_id: ObjectId):
    # Call the repository to get user by id
    user_data = await UserRepository.get_user_by_id(user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data


async def get_user_by_name_password(username: str, password: str) -> Optional[User]:
    user_data = await UserRepository.find_user_by_credentials(username, password)
    if user_data is None:
        raise HTTPException(status_code=401, detail="User not found or invalid username/password")
    return user_data


async def update_user_profile(user_id: int, user_data: User):
    # Check if user_id in path matches user_id in user_data
    if user_id != user_data.id:
        raise HTTPException(status_code=400, detail="User ID in path does not match user ID in body")
    # Using the is_valid_user method from the User model
    errors = user_data.is_valid_user()
    if errors:
        raise HTTPException(status_code=400, detail=errors)
    # Update user profile
    updated_user = await UserRepository.update_user(ObjectId(str(user_id)), user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
