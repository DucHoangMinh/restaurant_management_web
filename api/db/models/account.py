from .base import Base
import peewee as p
from . import db
class Accounts(Base):
    email = p.TextField()
    password = p.TextField()
    role = p.TextField()
    class Meta:
        db_table = 'accounts'
    @classmethod
    def create_account(cls, account):
        account = cls(
            email = account['email'],
            password = account['password'],
            role = account['role'],
        )
        try:
            account.save()
        except Exception as e:
            print(e)

    @classmethod
    def check_exists_account(cls, account):
        get_account = list(cls.select().where((cls.email == account.json['email']) & (cls.password == account.json['password'])))[0]
        return get_account.role if get_account else False

db.connect()
db.create_tables([Accounts], safe=True)
db.close()