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
    sex = p.TextField()
    phone = p.TextField()
    address = p.TextField()
    classroom = p.TextField()
    role = p.TextField()

    class Meta:
        db_table = 'user_infor'
    @classmethod
    def create_new_user(cls, request):
        student = cls(
            fullname=request.json['fullname'],
            dob=request.json['dob'],
            email=request.json['email'],
            sex=request.json['sex'],
            phone=request.json['phone'],
            address=request.json['address'],
            classroom=request.json['classroom'],
            role='student'
        )
        try:
            student.save(force_insert=True)
        except Exception as e:
            print('Error: ', e)
        Accounts.create_account({
            'email' : request.json['email'],
            'password':request.json['password'],
            'role': 'student'
        })
        return 'Create new student successful'

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
    def get_student_by_id(cls, id):
        getted_list = list(cls.select().where(cls.student_id == id))
        getted_student = getted_list[0] if len(getted_list) >= 1 else None
        return getted_student

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
