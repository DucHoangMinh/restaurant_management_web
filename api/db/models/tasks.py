import peewee as p
from . import db
from .base import Base
from flask import jsonify
from datetime import datetime
from playhouse.shortcuts import model_to_dict
from .students import Students
from .account import Accounts
import pytz

class Tasks(Base):
    task_id = p.AutoField(null=False)
    email = p.TextField(null=False)
    start = p.DateTimeField(null=False)
    end = p.DateTimeField(null=False)
    title = p.TextField(null=False)
    public = p.BooleanField(null=False)

    class Meta:
        db_table = 'tasklist'

    @classmethod
    def create_new_task(cls, request):
        get_student = list(Students.select().where(Students.email == request.json.get('email')))
        student = get_student[0]
        new_task = cls(
            email=request.json.get('email'),
            start=datetime.strptime(request.json['start'], "%Y-%m-%d %H:%M:%S"),
            end=datetime.strptime(request.json['end'], "%Y-%m-%d %H:%M:%S"),
            title= '[' +  student.fullname.upper() + '] ' + request.json['title'],
            public = True if str(request.json['public']) == 'True' else False
        )
        try:
            new_task.save()
        except Exception as e:
            print(e)
        return 'Successfully'
    @classmethod
    def get_all_tasks_by_email(cls, email):
        account = list(Accounts.select().where(Accounts.email == email))[0]
        list1 = list(cls.select().where(cls.public == True))
        list2 = list(cls.select().where(cls.email == email))
        list3 = list(cls.select())
        getted_list = list(set(list1 + list2))
        if(str(account.role) == 'teacher'):
            getted_list = list3

        # Đặt múi giờ mà bạn muốn chuyển đổi (ví dụ: 'Asia/Ho_Chi_Minh')
        desired_timezone = pytz.timezone('Asia/Ho_Chi_Minh')

        response = []

        for item in getted_list:
            # Chuyển đổi múi giờ của start và end trước khi trả về
            start_in_desired_timezone = pytz.timezone('UTC').localize(item.start)
            end_in_desired_timezone = pytz.timezone('UTC').localize(item.end)

            item_dict = model_to_dict(item)
            item_dict['start'] = start_in_desired_timezone.strftime('%Y-%m-%d %H:%M:%S')
            item_dict['end'] = end_in_desired_timezone.strftime('%Y-%m-%d %H:%M:%S')

            response.append(item_dict)

        return response
    @classmethod
    def get_task_by_id(cls,id):
        getted_task = cls.select().where(cls.task_id == id).first()
        return model_to_dict(getted_task)
    @classmethod
    def patch_task_by_id(cls,id,request):
        getted_task = list(cls.select().where(cls.task_id == id))[0]
        getted_task.email = request.json['email'],
        getted_task.start = datetime.strptime(request.json['start'], "%Y-%m-%d %H:%M:%S"),
        getted_task.end = datetime.strptime(request.json['end'], "%Y-%m-%d %H:%M:%S"),
        getted_task.title = request.json['title'],
        getted_task.public = request.json.get('public')
        try:
            getted_task.save()
        except Exception as e:
            print('Error : ', e)
        return jsonify('Success')

    @classmethod
    def delete_task_by_id(cls,id):
        try:
            querry = cls.delete().where(cls.task_id == id)
            querry.execute()
        except Exception as e:
            print(e)
        return "Deleted"

db.connect()
db.create_tables([Tasks], safe=True)
db.close()
