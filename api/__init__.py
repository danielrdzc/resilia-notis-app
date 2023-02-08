from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS()
cors.init_app(app, resources={r'/*': {'origins': '*'}})

from api.controllers.test import test_bp
app.register_blueprint(test_bp)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"