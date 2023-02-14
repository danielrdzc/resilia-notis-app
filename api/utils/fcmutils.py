import os
from typing import Any
from firebase_admin import messaging, credentials
import firebase_admin

class FCMUtils:
    def __init__(self):
        creds = credentials.Certificate(
        os.getcwd() + '/utils/wisptest-91d06-b58c766ff0d2.json')
        default_app = firebase_admin.initialize_app(creds)
    
    def send_to_token(registration_token, title, body, data=None) -> Any:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data,
            token=registration_token
        )
        response = messaging.send(message)
        return response