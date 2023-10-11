from flask import Flask
from flask_cors import CORS

def createApp():
    app = Flask(__name__)
    app.secret_key = "#@*(!#fdsfjkl;j)"
    CORS(app, supports_credentials=True)

    from app.sqlQuery.users import router as usersRouter

    app.register_blueprint(usersRouter, url_prefix='/') 

    return app