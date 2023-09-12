import peewee as p
from base import Base
from __init__ import db

class Teacher(Base):
    teacher_id = p.BigIntegerField()
    fullname = p.TextField()
    dob = p.DateField()
    email = p.TextField() 
    password = p.TextField()
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

    @staticmethod
    def verify_credentials(email, password):
        teacher = Teacher.get(Teacher.email == email)
        if teacher and teacher.password == password:
            return teacher
        return None

    def generate_access_token(self):
        access_token = create_access_token(identity=self.id)
        return access_token

db.connect()
db.create_tables([Teacher], safe=True)
db.close()
