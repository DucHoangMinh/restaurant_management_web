from db.models.teachers import Teacher
from flask import request, Blueprint
import string
from utils.controllers import token_required

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers/<email>', methods=['GET'])
@token_required
def get_teachers(email):
    return Teacher.get_teacher_by_email(email)