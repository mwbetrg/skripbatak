#qpy:console
import site
import os
from peewee import *
import time
import datetime
import io
import sys
# 20160103

if os.path.exists('/storage/extSdCard'):
    db = SqliteDatabase('/storage/extSdCard/mydb/lessonplan2010.db', **{})
    #backupdir = '/storage/extSdCard/dbbackup/'
    #db = '/storage/extSdCard/mydb/english-notes-exercises.sqlite'
else:
    db = SqliteDatabase('lessonplan2010.db', **{})


#db = SqliteDatabase('lessonplan2010.db', **{})
#db = SqliteDatabase('/storage/extSdCard/englishdb/lessonplan2010.db', **{})

class BaseModel(Model):
    class Meta:
        database = db


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



db.connect()

if len(sys.argv) < 4:
    print "Begini boh: %s minggu (WW) bulan (MM) hb (DD)" % sys.argv[0]
    sys.exit(1)

week = sys.argv[1]
month = sys.argv[2]
hb = int(sys.argv[3])
tahunini = datetime.datetime.now().year 
#tahunini = "2015"

tdatesun =  datetime.datetime(int(tahunini), int(month), int(hb)) + datetime.timedelta(days=0)
datesun = tdatesun.strftime('%Y%m%d')

#datesun = (str(tahunini)+str(month)+str(hb))

#-----------------------------------------------------------------------    
tdatemon = datetime.datetime(int(tahunini), int(month), int(hb)) + datetime.timedelta(days=1)
tdatetue = datetime.datetime(int(tahunini), int(month), int(hb)) + datetime.timedelta(days=2)
tdatewed = datetime.datetime(int(tahunini), int(month), int(hb)) + datetime.timedelta(days=3)
tdatethu = datetime.datetime(int(tahunini), int(month), int(hb)) + datetime.timedelta(days=4)

datemon = tdatemon.strftime('%Y%m%d')
datetue = tdatetue.strftime('%Y%m%d')
datewed = tdatewed.strftime('%Y%m%d')
datethu = tdatethu.strftime('%Y%m%d')                             

#-----------------------------------------------------------------------    
# Sunday

sun01 = Lessonplan2016.create(tingkatan="6AI3",\
                              date=int(datesun),\
                              timestart="0820",\
                              timeend="1020",\
                              duration="120",\
                              theme="-",\
                              topic="-",\
                              lo1="-",\
                              lo2="-",\
                              lo3="-",\
                              content="-",\
                              activity1="-",\
                              activity2="-",\
                              activity3="-",\
                              assimilation="-",\
                              impact="-",\
                              note="-",\
                              week=week,\
                              handout="-",\
                              exercise="-"
                             )

sun02 = Lessonplan2016.create(tingkatan="6AI5",\
                              date=datesun,\
                              timestart="1050",\
                              timeend="1250",\
                              duration="120",\
                              theme="-",\
                              topic="-",\
                              lo1="-",\
                              lo2="-",\
                              lo3="-",\
                              content="-",\
                              activity1="-",\
                              activity2="-",\
                              activity3="-",\
                              assimilation="-",\
                              impact="-",\
                              note="-",\
                              week=week,\
                              handout="-",\
                              exercise="-"
                             )

#-----------------------------------------------------------------------    
# Monday


mon01 = Lessonplan2016.create(tingkatan="6AI3",\
                              date=datemon,\
                              timestart="0900",\
                              timeend="1100",\
                              duration="120",\
                              theme="-",\
                              topic="-",\
                              lo1="-",\
                              lo2="-",\
                              lo3="-",\
                              content="-",\
                              activity1="-",\
                              activity2="-",\
                              activity3="-",\
                              assimilation="-",\
                              impact="-",\
                              note="-",\
                              week=week,\
                              handout="-",\
                              exercise="-"
                             )

mon02 = Lessonplan2016.create(tingkatan="6BI4",\
                              date=datemon,\
                              timestart="1130",\
                              timeend="1330",\
                              duration="120",\
                              theme="-",\
                              topic="-",\
                              lo1="-",\
                              lo2="-",\
                              lo3="-",\
                              content="-",\
                              activity1="-",\
                              activity2="-",\
                              activity3="-",\
                              assimilation="-",\
                              impact="-",\
                              note="-",\
                              week=week,\
                              handout="-",\
                              exercise="-"
                             )

#-----------------------------------------------------------------------    
# Tuesday

tue01 = Lessonplan2016.create(tingkatan="6AI5",\
                              date=datetue,\
                              timestart="0820",\
                              timeend="1020",\
                              duration="120",\
                              theme="-",\
                              topic="-",\
                              lo1="-",\
                              lo2="-",\
                              lo3="-",\
                              content="-",\
                              activity1="-",\
                              activity2="-",\
                              activity3="-",\
                              assimilation="-",\
                              impact="-",\
                              note="-",\
                              week=week,\
                              handout="-",\
                              exercise="-"
                             )

tue02 = Lessonplan2016.create(tingkatan="6AI3",\
                              date=datetue,\
                              timestart="1250",\
                              timeend="1410",\
                              duration="80",\
                              theme="-",\
                              topic="-",\
                              lo1="-",\
                              lo2="-",\
                              lo3="-",\
                              content="-",\
                              activity1="-",\
                              activity2="-",\
                              activity3="-",\
                              assimilation="-",\
                              impact="-",\
                              note="-",\
                              week=week,\
                              handout="-",\
                              exercise="-"
                             )

#-----------------------------------------------------------------------    
# Wednesday

wed01 = Lessonplan2016.create(tingkatan="6AI5",\
                              date=datewed,\
                              timestart="0740",\
                              timeend="0900",\
                              duration="80",\
                              theme="-",\
                              topic="-",\
                              lo1="-",\
                              lo2="-",\
                              lo3="-",\
                              content="-",\
                              activity1="-",\
                              activity2="-",\
                              activity3="-",\
                              assimilation="-",\
                              impact="-",\
                              note="-",\
                              week=week,\
                              handout="-",\
                              exercise="-"
                             )

wed02 = Lessonplan2016.create(tingkatan="6BI4",\
                              date=datewed,\
                              timestart="0940",\
                              timeend="1100",\
                              duration="80",\
                              theme="-",\
                              topic="-",\
                              lo1="-",\
                              lo2="-",\
                              lo3="-",\
                              content="-",\
                              activity1="-",\
                              activity2="-",\
                              activity3="-",\
                              assimilation="-",\
                              impact="-",\
                              note="-",\
                              week=week,\
                              handout="-",\
                              exercise="-"
                             )


#-----------------------------------------------------------------------    
# Thursday

thu01 = Lessonplan2016.create(tingkatan="6BI4",\
                              date=datethu,\
                              timestart="1210",\
                              timeend="1410",\
                              duration="120",\
                              theme="-",\
                              topic="-",\
                              lo1="-",\
                              lo2="-",\
                              lo3="-",\
                              content="-",\
                              activity1="-",\
                              activity2="-",\
                              activity3="-",\
                              assimilation="-",\
                              impact="-",\
                              note="-",\
                              week=week,\
                              handout="-",\
                              exercise="-"
                             )

thisweek = Lessonplan2016.select().where(Lessonplan2016.week == week)

for i in thisweek:
    print str(i.date)+" = "+i.timestart
