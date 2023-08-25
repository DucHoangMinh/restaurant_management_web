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


db.connect()
db.create_tables([Students], safe=True)
db.close()
# print((Students.get_all_students()))
