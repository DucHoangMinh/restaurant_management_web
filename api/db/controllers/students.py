from db.models.students import Students
from flask import request, Blueprint
import random
import string
from utils.controllers import token_required
students_bp = Blueprint('students', __name__)


@students_bp.route('/students', methods=['GET'])
def get_all_students():
    return Students.get_all_students()


@students_bp.route('/students', methods=['POST'])
def create_student():
    return Students.create_new_students(request)


@students_bp.route('/students/<email>', methods=['GET'])
@token_required
def get_student_by_email(email):
    return Students.get_student_by_email(email)


@students_bp.route('/students/<id>', methods=['PATCH'])
@token_required
def patch_student_byid(id):
    return Students.patch_student_by_id(request, id)
@students_bp.route('/students/<email>', methods=['DELETE'])
def delete_student_by(email):
    return Students.delete_student(email)
