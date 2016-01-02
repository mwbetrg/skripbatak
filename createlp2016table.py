import site
import sys, os
from peewee import *
import datetime
import time
import calendar
import sqlite3
import gzip
import shutil

#-----------------------------------------------------------------------    

if os.path.exists('/storage/extSdCard'):
    database = SqliteDatabase('/storage/extSdCard/mydb/lessonplan2010.db', **{})
    backupdir = '/storage/extSdCard/dbbackup/'
    db = '/storage/extSdCard/mydb/lessonplan2010.db'
else:
    database = SqliteDatabase('lessonplan2010.db', **{})


class BaseModel(Model):
    class Meta:
        database = database

class Lessonplanbank(BaseModel):
    activity1 = CharField(null=True)
    activity2 = CharField(null=True)
    assimilation = CharField(null=True)
    bank = PrimaryKeyField(db_column='bank_id', null=True)
    content = CharField(null=True)
    duration = CharField(null=True)
    exercise = TextField(null=True)
    handout = TextField(null=True)
    impact = CharField(null=True)
    level = CharField(null=True)
    lo1 = CharField(null=True)
    lo2 = CharField(null=True)
    lo3 = CharField(null=True)
    note = CharField(null=True)
    theme = CharField(null=True)
    tingkatan = CharField(null=True)
    topic = CharField(null=True)
    week = IntegerField(null=True)

    class Meta:
        db_table = 'lessonplanbank'

class Lessonplan2016(BaseModel):
    activity1 = CharField(null=True)
    activity2 = CharField(null=True)
    assimilation = CharField(null=True)
    content = CharField(null=True)
    date = IntegerField(null=True)
    duration = CharField(null=True)
    exercise = TextField(null=True)
    handout = TextField(null=True)
    impact = CharField(null=True)
    lo1 = CharField(null=True)
    lo2 = CharField(null=True)
    lo3 = CharField(null=True)
    note = CharField(null=True)
    theme = CharField(null=True)
    timeend = CharField(null=True)
    timestart = CharField(null=True)
    tingkatan = CharField(null=True)
    topic = CharField(null=True)
    week = CharField(null=True)

    class Meta:
        db_table = 'lessonplan2016'

database.connect()

def create_tables():
    database.connect()
    database.create_tables([Lessonplan2016,])

create_tables()
