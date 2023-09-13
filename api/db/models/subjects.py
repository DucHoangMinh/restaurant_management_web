import peewee as p
from . import db
from .base import Base
from flask import jsonify
from playhouse.shortcuts import model_to_dict
from .account import Accounts
class Subject(Base):
    subject_id = p.AutoField(primary_key=True)
    name = p.TextField()
    description = p.TextField()
    grade=p.IntegerField()

    class Meta:
        db_table = 'subjects'
    @classmethod
    def get_subject_by_id(cls, id):
        return jsonify(model_to_dict(list(cls.select().where(cls.subject_id == id))[0]))

db.connect()
db.create_tables([Subject], safe=True)
db.close()
    