from flask import request, jsonify, Blueprint
from app.modules.conn import createUsers, selectUsers
import random

router = Blueprint('usersRouter', __name__)


def index():
    if not request.get_json('password'):
        return jsonify({'alert': 'session not found!'}), 404

    print(request.get_json('password'))
    response = jsonify({'password': request.get_json('password')})
    return response, 200

# 登入


@router.route('/login', methods=['POST'])
def login():
    try:
        if request.method == 'POST':
            account = request.get_json()['account']
            password = request.get_json()['password']
            sqlQuery = f"SELECT * FROM users WHERE Account = '{account}' AND Password = '{password}';"
            result = selectUsers(sqlQuery)
            if not result:
                return jsonify({'alert': 'not data'}), 404
        print(result)
        return jsonify({'password': password}), 201

    except Exception as e:
        print(e)
        return '', 404

# 新增帳戶


@router.route('/create', methods=['POST'])
def create():
    try:
        if request.method == 'POST':
            account = request.get_json()['account']
            password = request.get_json()['password']
            idNumber = random.randrange(32767)
            sqlQuery = f"INSERT INTO users(ID, Account, Password) \
                        VALUES('{idNumber}' ,'{account}', '{password}');"
            createUsers(sqlQuery)
            return jsonify({'ID': idNumber,
                            'account': account,
                            'password': password}), 201
        return jsonify({'alert': 'not data'}), 404

    except Exception as e:
        print(e)
        return '', 404
