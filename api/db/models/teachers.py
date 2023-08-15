import peewee as p
from base import Base


class Teacher(Base):
    id = p.BigIntegerField().primary_key
    fullname = p.TextField()
    role = p.TextField()
    dob = p.DateField()

    class Meta:
        db_table = 'teachers'


Teacher.create_table()
