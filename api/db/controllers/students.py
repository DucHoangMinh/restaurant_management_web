from db.models.students import Students
from flask import request, Blueprint
import random
import string

students_bp = Blueprint('students', __name__)


@students_bp.route('/students', methods=['GET'])
def get_all_students():
    print("how")
    return Students.get_all_students()


@students_bp.route('/students', methods=['POST'])
def create_student():
    print(request)
    student = Students(
        fullname=request.json['fullname'],
        dob=request.json['dob'],
        email=request.json['email'],
        sex=request.json['sex'],
        phone=request.json['phone'],
        address=request.json['address'],
        date_of_join=request.json.get('date_of_join'),
        password=request.json.get('password')
    )
    try:
        student.save()
    except Exception as e:
        print('Error: ', e)
    return student.password


@students_bp.route('/students/<email>', methods=['GET'])
def get_student_by_id(email):
    return Students.get_student_by_id(email)


@students_bp.route('/students/<id>', methods=['PATCH'])
def patch_student_byid(id):
    return Students.patch_student_by_id(request, id)
@students_bp.route('/students/<email>', methods=['DELETE'])
def delete_student_by(email):
    return Students.delete_student(email)
