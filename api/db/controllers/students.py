from db.models.students import Students
from flask import  request, Blueprint
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
        date_of_join=request.json.get('date_of_join', '01-01-2001'),
        password='default'
    )
    try:
        student.save()
    except Exception as e:
        print('Error: ', e)
    return student.password
