from typing import Union
from fastapi import FastAPI
from routers import user, login, commissionrequest, usernotification
from fastapi.middleware.cors import CORSMiddleware
from utils.fcmutils import FCMUtils

app = FastAPI()

messaging = FCMUtils()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(login.router)
app.include_router(commissionrequest.router)
app.include_router(usernotification.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}