import peewee as p
from . import db
from .base import Base
from flask import jsonify
from playhouse.shortcuts import model_to_dict
from .students import Students
from .account import Accounts
class Student_Classroom(Base):
    student_id = p.BigIntegerField(null=False)
    classroom_id = p.BigIntegerField(null=False)
    class Meta:
        db_table = 'student_classroom'
    @classmethod
    def get_student_in_classroom(cls,id):
        student_list = list(cls.select().where(cls.classroom_id == id))
        student_list2 = []
        for i in range(0, len(student_list)):
            student = Students.get_student_by_id(student_list[i].student_id)
            student_list[i] = student
        get_list = [model_to_dict(item) for item in student_list]
        return get_list


db.connect()
db.create_tables([Student_Classroom], safe=True)
db.close()
