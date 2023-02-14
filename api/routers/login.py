from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import UserModel
from schemas import LoginBaseSchema

router = APIRouter(
    prefix='/api'
)

@router.post('/login')
def login(payload: LoginBaseSchema, db: Session = Depends(get_db)):
    query = db.query(UserModel).filter(
        UserModel.username==payload.username,
        UserModel.password==payload.password    
    )
    user_model = query.first()
    if not user_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='No user found')
    query.update({'fcmtoken': payload.fcmtoken}, synchronize_session=False)
    db.commit()
    db.refresh(user_model)
    #FCMUtils.send_to_token(payload.fcmtoken, 'ola k ase', 'cuerpooooo')
    
    return { "status": "Success - Logged in", "data": user_model }