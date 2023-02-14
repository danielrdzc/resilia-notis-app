from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from database import get_db
from models import UserModel
from schemas import UserBaseSchema

router = APIRouter(
    prefix='/api/user',
    tags=["user"]
)

@router.get('/artists')
def get_all_artists(db: Session = Depends(get_db)):
    artists = db.query(UserModel).filter(
        UserModel.role == 1).all()
    return { "status": "Success", "data": artists }

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(payload: UserBaseSchema, db: Session = Depends(get_db)):
    new_user = UserModel(**payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return { "status": "Success - user created", "data": new_user }
