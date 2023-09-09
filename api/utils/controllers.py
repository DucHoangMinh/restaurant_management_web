from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv
import jwt
load_dotenv()
import os

SECRET_KEY= 'g}/lVKCOmv)kvhWBNV;+}_}.eJ(]n`Y:d,O|q44lgMIHeHp|G;27>KS2,ynEDhJ'
def token_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'Alert': 'Token is missing'})
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except Exception as e:
            return jsonify({'Alert': 'Token is invalid'})
        return func(*args, **kwargs)

    return decorator
