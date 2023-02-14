from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from database import get_db
from models import CommissionRequestModel, UserNotificationModel
from schemas import CommissionRequestBaseSchema
from utils.fcmutils import FCMUtils

router = APIRouter(
    prefix='/api/commission_request',
    tags=["commision_request"]
)


@router.get('/pending')
def get_pending_commission_requests(user_id: int, db: Session = Depends(get_db)):
    pending_commission_requests = db.query(CommissionRequestModel).filter(
        or_(CommissionRequestModel.requesting_user_id == user_id,
                CommissionRequestModel.artist_user_id == user_id),
        CommissionRequestModel.status == 1
    ).all()
    return { "status": "Success", "data": pending_commission_requests }


@router.get('/ongoing')
def get_ongoing_commission_requests(user_id: int, db: Session = Depends(get_db)):
    ongoing_commission_requests = db.query(CommissionRequestModel).filter(
        or_(CommissionRequestModel.requesting_user_id == user_id,
                CommissionRequestModel.artist_user_id == user_id),
        CommissionRequestModel.status == 2
    ).all()
    return { "status": "Success", "data": ongoing_commission_requests }


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_commission_request(payload: CommissionRequestBaseSchema, db: Session = Depends(get_db)):
    # TODO: ADD TRANSACTIONS
    new_commission_request = CommissionRequestModel(**payload.dict())
    db.add(new_commission_request)
    db.commit()
    db.refresh(new_commission_request)

    #notification
    fcmtoken = new_commission_request.artist_user.fcmtoken
    # commission_type = ''
    # if new_commission_request.request_type == 1:
    #     commission_type = 'Sculpture'
    # elif new_commission_request.request_type == 2:
    #     commission_type = 'Painting'
    # elif new_commission_request.request_type == 3:
    #     commission_type = 'Other'
    noti_title = 'New Commission Request!'
    noti_content = 'The company ' + new_commission_request.requesting_user.name + ' wants to work with you!'
    user_notification = UserNotificationModel()
    user_notification.user_id = payload.artist_user_id
    user_notification.title = noti_title
    user_notification.content = noti_content
    user_notification.notification_type = 1

    db.add(user_notification)
    db.commit()
    db.refresh(user_notification)

    FCMUtils.send_to_token(fcmtoken, noti_title, noti_content)
    return { "status": "Success - commission request created", "data": new_commission_request }


@router.put('/{commission_request_id}')
def update_commission_request(commission_request_id: int, payload: CommissionRequestBaseSchema, db: Session = Depends(get_db)):
    # TODO: ADD TRANSACTIONS
    query = db.query(CommissionRequestModel).filter(
        CommissionRequestModel.id == commission_request_id
    )
    commission_request = query.first()
    if not commission_request:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail = 'No Commission Request found')

    update_data = payload.dict(exclude_unset=True)
    query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(commission_request)
    
    #notification
    fcmtoken = commission_request.requesting_user.fcmtoken
    commission_status = ''
    if commission_request.status == 2:
        commission_status = 'ACCEPTED'
    elif commission_request.status == 3:
        commission_status = 'REJECTED'
    
    noti_title = 'Your artist has responded!'
    noti_content = 'The artist ' + commission_request.artist_user.name + ' has ' + commission_status + ' your commission request.'
    user_notification = UserNotificationModel()
    user_notification.user_id = commission_request.requesting_user_id
    user_notification.title = noti_title
    user_notification.content = noti_content
    user_notification.notification_type = 1

    db.add(user_notification)
    db.commit()
    db.refresh(user_notification)

    FCMUtils.send_to_token(fcmtoken, noti_title, noti_content)
    return { "status": "Success - Commission Request Updated", "data": commission_request }