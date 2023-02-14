from datetime import datetime
from typing import Union
from pydantic import BaseModel

class LoginBaseSchema(BaseModel):
    username: str
    password: str
    fcmtoken: str

class UserBaseSchema(BaseModel):
    id: Union[int, None] = None
    name: str
    username: str
    password: str
    role: int

class CommissionRequestBaseSchema(BaseModel):
    id: Union[int, None] = None
    requesting_user_id: Union[int, None] = None
    artist_user_id: Union[int, None] = None
    request_type: Union[int, None] = None
    status: Union[int, None] = None
    createdDt: Union[datetime, None] = None