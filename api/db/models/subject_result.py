import peewee as p
from . import db
from .base import Base
from flask import jsonify
from playhouse.shortcuts import model_to_dict
class Subject_Result(Base):
    subject_id = p.BigIntegerField(primary_key=True)
    classroom_id = p.BigIntegerField(null=False)
    student_id = p.BigIntegerField(null=False)
    point = p.IntegerField(null=False)
    class Meta:
        db_table = 'student_result'
    @classmethod
    def input_result(cls, request):
        temp = cls(
            subject_id=1,
            classroom_id=1,
            student_id=1,
            point=1
        )
        temp.save()
        return jsonify('Success')




db.connect()
db.create_tables([Subject_Result], safe=True)
db.close()