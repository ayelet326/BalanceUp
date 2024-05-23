from fastapi import FastAPI
import uvicorn
from app.routers.userRouter import userRouter

app = FastAPI()

app.include_router(userRouter,prefix='/user')

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
