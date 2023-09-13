from peewee import Model
from . import  db

class Base(Model):
    class Meta:
        database = db
        legacy_table_names = False
        only_save_dirty = True