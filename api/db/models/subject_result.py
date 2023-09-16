import peewee as p
from . import db
from .base import Base
from flask import jsonify
from playhouse.shortcuts import model_to_dict
class Subject_Result(Base):
    subject_id = p.BigIntegerField()
    classroom_id = p.BigIntegerField()
    student_id = p.BigIntegerField()
    point = p.IntegerField()
    class Meta:
        db_table = 'student_result'
    @classmethod
    def input_result(cls, request):
        new_point = cls(
            subject_id=1,
            classroom_id=1,
            student_id=1,
            point=1
        )
        try:
            new_point.save()
            db.commit()
        except Exception as e:
            print(e)
        return jsonify('Success')




db.connect()
db.create_tables([Subject_Result], safe=True)
db.close()