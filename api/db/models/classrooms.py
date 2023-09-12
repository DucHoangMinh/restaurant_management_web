import peewee as p
from . import db
from .base import Base
from flask import jsonify
from datetime import datetime
from playhouse.shortcuts import model_to_dict

class Classrooms(Base):
    classroom_id = p.AutoField(null=False)
    classroom_name = p.TextField(null=False)
    teacher_id = p.IntegerField(null=False)
    grade = p.IntegerField(null=False)

    class Meta:
        db_table = 'classrooms'

db.connect()
db.craeate_tables([Classrooms],safe=True)
db.close()