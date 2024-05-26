from bson import ObjectId
from fastapi import FastAPI, Depends, APIRouter

from app.models.user import User
from app.services import userService

userRouter = APIRouter()


@userRouter.get("/hello")
def func():
    return "hello world"


@userRouter.post("/signUp")
async def SignUp(user: User):
    await userService.create_user(user)
    return {"message": "User created successfully"}


@userRouter.post("/signIn")
async def signIn(name: str, password: str):
    user = await userService.get_user_by_name_password(name, password)
    if user:
        return {"message": "Sign-in successful", "userId": user.id}


@userRouter.put("/{user_id}")
async def edit_profile(user_id: int, user_data: User):
    await userService.update_user_profile(user_id, user_data)
    return {"message": "User profile updated successfully"}
