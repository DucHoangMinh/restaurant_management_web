from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase
from config import POSTGRE_DATABASE, POSTGRE_HOST, POSTGRE_USER, POSTGRE_PASSWORD

db = PostgresqlExtDatabase(
    POSTGRE_DATABASE,
    user=POSTGRE_USER,
    password=POSTGRE_PASSWORD,
    host=POSTGRE_HOST,
    autorollback=True
)
