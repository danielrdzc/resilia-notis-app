from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from database import get_db
from models import UserNotificationModel


router = APIRouter(
    prefix='/api/user_notification',
    tags=["user_notification"]
)

@router.get('/all')
def get_all_user_notifications(user_id: int, db: Session = Depends(get_db)):
    user_notification = db.query(UserNotificationModel).filter(
        UserNotificationModel.user_id == user_id).all()
    return { "status": "Success", "data": user_notification }