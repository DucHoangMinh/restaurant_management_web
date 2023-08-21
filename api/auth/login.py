# flask imports
from flask import Flask, request, jsonify, make_response
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from db.models.teachers import Teacher
import db
from db.models import db

# creates Flask object
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '123456'
jwt = JWTManager(app)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    teacher = Teacher.verify_credentials(data['email'], data['password'])

    if teacher:
        access_token = teacher.generate_access_token()
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/', methods=['GET'])
def test():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)