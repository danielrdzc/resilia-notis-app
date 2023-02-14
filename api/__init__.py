# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_cors import CORS
# from flask_restful import Api

# db = SQLAlchemy()

# app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:3306/resillia_notis_app"

# db.init_app(app)

# migrate = Migrate(app, db)

# api = Api(app, prefix='/api')

# cors = CORS()
# cors.init_app(app, resources={r'/*': {'origins': '*'}})

# from api.models import UserModel, CommissionRequestModel

# from api.controllers.test import test_bp
# from api.controllers.user import User

# api.add_resource(User, '/', endpoint='user')
# app.register_blueprint(test_bp)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
# from typing import Union
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}