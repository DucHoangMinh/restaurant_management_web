import peewee as p
from .base import Base
from . import db
from flask import jsonify
from playhouse.shortcuts import model_to_dict

class Teacher(Base):
    teacher_id = p.BigIntegerField()
    fullname = p.TextField()
    dob = p.DateField()
    email = p.TextField()
    sex = p.BooleanField()
    phone = p.BigIntegerField()
    date_of_join = p.DateField()


    class Meta:
        db_table = 'teachers'
    @classmethod
    def get_all_teachers(cls):
        teacherList = []
        teachers = list(cls.select())
        for teacher in teachers:
            teacherList.append(teacher[0])
        return teacherList

    @classmethod
    def get_teacher_by_email(cls, email):
        getted_list = list(cls.select().where(cls.email == email))
        getted_teacher = getted_list[0] if len(getted_list) >= 1 else None
        return jsonify(model_to_dict(getted_teacher))


    # @staticmethod
    # def verify_credentials(email, password):
    #     teacher = Teacher.get(Teacher.email == email)
    #     if teacher and teacher.password == password:
    #         return teacher
    #     return None
    #
    # def generate_access_token(self):
    #     access_token = create_access_token(identity=self.id)
    #     return access_token
db.connect()
db.create_tables([Teacher], safe=True)
db.close()
