from typing import List
from bson import ObjectId
from fastapi import HTTPException

from ..db_manegement.repositories import user_repository as UserRepository
from ..models import user


def create_user(user_data: user) -> ObjectId:
        # Here you can implement your validation logic
        if not user_data.get("email"):
            raise HTTPException(status_code=400, detail="Email is required")

        # You can implement additional validations here

        # Call the repository to insert the user
        user_id = UserRepository.create_user(user_data)
        return user_id

def get_user_by_id(user_id: ObjectId):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

