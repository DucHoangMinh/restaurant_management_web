import peewee as p
from . import db
from .base import Base
from flask import jsonify
from playhouse.shortcuts import model_to_dict

class Students(Base):
    student_id = p.AutoField(primary_key=True)
    fullname = p.TextField()
    dob = p.DateField()
    email = p.TextField()
    password = p.TextField()
    sex = p.TextField()
    phone = p.BigIntegerField()
    address = p.TextField()
    date_of_join = p.DateField()

    class Meta:
        db_table = 'students'

    @classmethod
    def get_all_students(cls):
        get_list = list(cls.select())
        students_list = [model_to_dict(student) for student in get_list]
        return students_list
    @classmethod
    def get_student_by_id(cls,email):
        get_student = list(cls.select().where(cls.email == email))
        return jsonify(model_to_dict(get_student[0]))
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
# print((Students.get_all_students()))
