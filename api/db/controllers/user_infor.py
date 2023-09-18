from db.models.user_infor import Students
from flask import request, Blueprint
import random
import string
from utils.controllers import token_required
students_bp = Blueprint('students', __name__)


@students_bp.route('/user_infor', methods=['GET'])
def get_all_students():
    return Students.get_all_students()


@students_bp.route('/user_infor', methods=['POST'])
def create_student():
    return Students.create_new_user(request)


@students_bp.route('/user_infor/<email>', methods=['GET'])
@token_required
def get_student_by_email(email):
    return Students.get_student_by_email(email)


@students_bp.route('/user_infor/<id>', methods=['PATCH'])
@token_required
def patch_student_byid(id):
    return Students.patch_student_by_id(request, id)
@students_bp.route('/user_infor/<email>', methods=['DELETE'])
def delete_student_by(email):
    return Students.delete_student(email)
