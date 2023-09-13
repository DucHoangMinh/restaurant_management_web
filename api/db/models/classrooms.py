import peewee as p
from . import db
from .base import Base
from flask import jsonify
from datetime import datetime
from playhouse.shortcuts import model_to_dict

class Classroom(Base):
    classroom_id = p.AutoField(null=False)
    classroom_name = p.TextField(null=False)
    teacher_id = p.IntegerField(null=False)
    grade = p.IntegerField(null=False)

    class Meta:
        db_table = 'classrooms'
    @classmethod
    def get_classroom_by_id(cls,id):
        return jsonify(model_to_dict(list(cls.select().where(cls.classroom_id == id))[0]))
    @classmethod
    def get_classroom_by_teacher_id(cls,id):
        get_list = list(cls.select().where(cls.teacher_id == id))
        class_list = [model_to_dict(item) for item in get_list]
        return class_list
db.connect()
db.create_tables([Classroom],safe=True)
db.close()