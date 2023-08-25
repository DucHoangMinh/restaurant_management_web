from db.models.students import Students
from main import app
from flask import  request
import random
import string


@app.route('/students', methods=['GET'])
def get_all_students():
    return Students.get_all_students()


@app.route('/students', methods=['POST'])
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
