from fastapi import FastAPI, Depends, APIRouter

userRouter = APIRouter()


@userRouter.get("/hello")
def func():
    return "hello world"
