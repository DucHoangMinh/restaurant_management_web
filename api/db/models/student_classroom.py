import peewee as p
from . import db
from .base import Base
from flask import jsonify
from playhouse.shortcuts import model_to_dict
from .account import Accounts
class Student_Classroom(Base):
    student_id = p.BigIntegerField(null=False)
    classroom_id = p.BigIntegerField(null=False)
