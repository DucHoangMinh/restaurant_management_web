# flask imports
from flask import Flask, request, jsonify, make_response,render_template,session, Blueprint
import jwt
from datetime import datetime, timedelta
from functools import wraps
from db.models.account import Accounts
login_bp = Blueprint('login', __name__)

@login_bp.route('/auth')
# @token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard !  '
