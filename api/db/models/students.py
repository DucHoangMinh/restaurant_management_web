import peewee as p
from . import db
from .base import Base
from flask import jsonify
from playhouse.shortcuts import model_to_dict
from .account import Accounts
class Students(Base):
    student_id = p.AutoField(primary_key=True)
    fullname = p.TextField()
    dob = p.DateField()
    email = p.TextField()
    password = p.TextField()
    sex = p.TextField()
    phone = p.TextField()
    address = p.TextField()
    date_of_join = p.DateField()

    class Meta:
        db_table = 'students'
    @classmethod
    def create_new_students(cls, request):
        student = cls(
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
        Accounts.create_account({
            'email' : student.email,
            'password':student.password,
            'role': 'student'
        })
        return student.password

    @classmethod
    def get_all_students(cls):
        get_list = list(cls.select())
        students_list = [model_to_dict(student) for student in get_list]
        return students_list
    @classmethod
    def get_student_by_email(cls,email):
        getted_list = list(cls.select().where(cls.email == email))
        getted_student = getted_list[0] if len(getted_list) >= 1 else None
        return jsonify(model_to_dict(getted_student))

    @classmethod
    def patch_student_by_id(cls, request, id):
        student = list(cls.select().where(cls.student_id == id))[0]
        student.fullname = request.json.get('fullname')
        student.email = request.json.get('email')
        student.dob = request.json.get('dob')
        student.sex = request.json.get('sex')
        student.phone =request.json.get('phone')
        student.date_of_join = request.json.get('date_of_join')
        student.address = request.json.get('address')
        try:
            student.save()
        except Exception as e:
            print("Failed to save student ", e)
        return "Done!"

    @classmethod
    def delete_student(cls, email):
        try:
            querry = cls.delete().where(cls.email == email)
            querry.execute()
        except Exception as e:
            print("Failed to delete student ", e)
        return "Deleted"

db.connect()
db.create_tables([Students], safe=True)
db.close()
