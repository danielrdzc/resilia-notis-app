from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base

class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    username = Column(String(250), unique=True, index=True)
    password = Column(String(250))
    role = Column(Integer)
    fcmtoken = Column(String(1000))

class CommissionRequestModel(Base):
    __tablename__ = 'commission_request'
    id = Column(Integer, primary_key=True, index=True)
    requesting_user_id = Column(Integer, ForeignKey('user.id'))
    requesting_user = relationship('UserModel', foreign_keys=[requesting_user_id])
    artist_user_id = Column(Integer, ForeignKey('user.id'))
    artist_user = relationship('UserModel', foreign_keys=[artist_user_id])
    request_type = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    createdDt = Column(DateTime, default=datetime.now)

class UserNotificationModel(Base):
    __tablename__ = 'user_notification'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', foreign_keys=[user_id])
    content = Column(String(1000))
    notification_type = Column(Integer, nullable=False)
    createdDt = Column(DateTime, default=datetime.now)
    title = Column(String(250))