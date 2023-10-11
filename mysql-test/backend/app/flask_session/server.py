from flask import Flask, request, Blueprint, jsonify, session
from flask.sessions import SecureCookieSessionInterface
from flask_cors import CORS
from flask_session import Session
from ..modules.conn import createUsers

app = Flask(__name__)
app.secret_key = "#@*(!#fdsfjkl;j)"

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"

# Session Cookie 設定
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = True

# 處理 samesite=None 的問題
session_cookie = SecureCookieSessionInterface.get_signing_serializer(
    self=SecureCookieSessionInterface, app=app)
CORS(
    app=app,
    supports_credentials=True,
)
Session(app)

# 取得session
@app.route('/')
def index():
    if not session.get('password'):
        return jsonify({'alert': 'session not found!'}), 404

    print(session['password'])
    response = jsonify({'password': session['password']})
    return response, 200

# 登入
@app.route('/login', methods=['POST'])
def login():
    try:
        password = request.get_json()['password']
        print('loginpassword', password)
        session['password'] = password
        return jsonify({'password': session['password']}), 201

    except Exception as e:
        print(e)
        return '', 404
    
# 新增帳戶
@app.route('/create', methods=['POST'])
def create():
    try:
        data = request.json
        account = data['account']
        password = data['password']
        sqlQuery = f"INSTER INTO users(Account, Password) \
                    VALUES('{account}', '{password}');"
        createUsers(sqlQuery)

    except Exception as e:
        print(e)
        return '', 404


if __name__ == '__main__':
    app.run(debug='True')
