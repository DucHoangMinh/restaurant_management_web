from flask_cors import CORS
from db.controllers.students import students_bp
from db.controllers.tasks import tasks_bp
from auth.login import login_bp
from flask import Flask, request, jsonify, make_response,render_template,session, Blueprint
import jwt
from datetime import datetime, timedelta
from functools import wraps
from db.models.account import Accounts
from dotenv import load_dotenv
from utils.controllers import token_required
load_dotenv()
import os
SECRET_KEY=os.getenv('SECRET_KEY')
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
CORS(app)

app.register_blueprint(students_bp)
app.register_blueprint(login_bp)
app.register_blueprint(tasks_bp)


@app.route('/login', methods=['POST'])
def handle_login():
    if Accounts.check_exists_account(request): #Đoạn này để handle nếu email và password có trong cơ sở dữ liệu
        session['logged_in'] = True
        token = jwt.encode({
            'user': request.json['email'],
            'expiration': str(datetime.utcnow() + timedelta(seconds=12000))
        }, app.config['SECRET_KEY'])
        return jsonify(
            {'token': token},
            {'email': request.json['email']}
        )
    else:
        return make_response('Unable to verify' ,403,{'WWW-Authenticate': 'Basic realm: Authentication Failed'})

@app.route('/', methods=['GET'])
def test():
    return 'API RESPONSE SUCCESS !!!'

@app.route('/testtoken', methods=['GET'])
@token_required
def getget():
    try:
        return make_response('Hoang Minh Duc')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')