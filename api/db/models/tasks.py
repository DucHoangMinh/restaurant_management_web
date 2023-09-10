import peewee as p
from . import db
from .base import Base
from flask import jsonify
from datetime import datetime
from playhouse.shortcuts import model_to_dict


class Tasks(Base):
    task_id = p.AutoField(null=False)
    email = p.TextField(null=False)
    start = p.DateTimeField(null=False)
    end = p.DateTimeField(null=False)
    title = p.TextField(null=False)
    done = p.BooleanField(null=False)

    class Meta:
        db_table = 'tasklist'

    @classmethod
    def create_new_task(cls, request):
        new_task = cls(
            email=request.json.get('email'),
            start=datetime.strptime(request.json['start'], "%Y-%m-%d %H:%M:%S"),
            end=datetime.strptime(request.json['end'], "%Y-%m-%d %H:%M:%S"),
            title=request.json['title'],
            done=True
        )
        try:
            new_task.save()
        except Exception as e:
            print(e)
        return 'Successfully'
    @classmethod
    def get_all_tasks_by_email(cls, email):
        getted_list = (list(cls.select().where(cls.email==email)))
        response = [model_to_dict(item) for item in getted_list]
        return response
db.connect()
db.create_tables([Tasks], safe=True)
db.close()
