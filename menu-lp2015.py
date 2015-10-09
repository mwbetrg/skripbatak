#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :This program displays an interactive menu on CLI
#author          :
#date            :
#version         :0.1
#usage           :python menu.py
#notes           :
#python_version  :2.7.6  
#=======================================================================

#qpy:2
#qpy:console

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

class Lessonplan2015(BaseModel):
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
        db_table = 'lessonplan2015'

database.connect()

#-----------------------------------------------------------------------    

tahunini = datetime.datetime.today().year
hariini = datetime.datetime.today()
harini = hariini.strftime("%Y%m%d")

# Main definition - constants
menu_actions  = {}  

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    
    print ":: LP 2015 ::\n"
    print "Sila pilih menu yang dikehendaki:"
    print "1. Menu 1"
    print "2. Menu 2"
    print "3. Cari tarikh LP 2015"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Menu 1
def menu1():
    print "Menu LP 2015 !\n"
    print "9. Kembali"
    print "0. Keluar"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Menu 2
def menu2():
    print "Hello Menu 2 !\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

#-----------------------------------------------------------------------    

def peliharadata():
    reload(sys)
    sys.setdefaultencoding('utf8')
    con = sqlite3.connect(db)
    with open(backupdir+'dump-lp2015-'+harini+'.sql', 'w') as f:
        for line in con.iterdump():
            f.write('%s\n' % line)
    with open(backupdir+'dump-lp2015-'+harini+'.sql', 'rb') as f_in, gzip.open(backupdir+'dump-lp2015-'+harini+'.sql.gz', 'wb') as f_out :
        shutil.copyfileobj(f_in, f_out)
    failhantar = backupdir+'dump-lp2015-'+harini+'.sql'
    os.remove(failhantar)
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Masuk Lesson Bank

def masuklessonplanbank():
    def masukpengkalandata():
        q = Lessonplanbank.insert(tingkatan=form, level=level, week=week,\
                          duration=duration, theme=theme, topic=topic,\
                          lo1=lo1, lo2=lo2, lo3=lo3,\
                          content=content, activity1=activity1,\
                          activity2=activity2,\
                          assimilation=assimilation, impact=impact, note=note)
        q.execute()

    sempang = "-"
    cuti  = "Cuti Umum"
    semua = "All"
    #tahunini = strftime("%Y")

    print "\nEnter type of entry\n"
    print "--Ordinary     :<CR>\n"
    print "--Exam         :  e\n"
    print "--Holiday      :  h\n"
    print "--Long Holiday :  l\n"
    print "--Special Event:  s\n"
    print "--Outstation   :  o\n"
    print "--Extra Class   :  x\n\n"

    entry = raw_input("Enter type of entry: \n")

    if entry.startswith("e"):
        form = raw_input("Enter CLASS: \n")
        week = raw_input("Enter WEEK: \n")
        duration = raw_input("Enter DURATION: \n")
        subtheme = raw_input("Enter EXAM (e.g. TOV / PERTENGAHAN - without \"PEPERIKSAAN\"\n")
        periksa = "PEPERIKSAAN"
        theme = periksa  + " " + subtheme
        topic = raw_input("Enter SUBJECT: \n")
        lo1 = raw_input("Enter TIME: \n")
        lo2 = raw_input("Enter DURATION OF EXAM: \n")
        level = sempang
        lo3 = sempang
        content = sempang
        activity1 = sempang
        activity2 = sempang
        assimilation = sempang
        impact = sempang
        note = sempang
        masukpengkalandata()

    elif entry.startswith("h"):
        week = raw_input("Enter WEEK: \n")
        duration = sempang
        theme = cuti
        topic = raw_input("Enter Holiday\n")
        topic.replace("'","''")
        lo1 = sempang
        lo2 = sempang
        form = semua
        level = sempang
        lo3 = sempang
        content = sempang
        activity1 = sempang
        activity2 = sempang
        assimilation = sempang
        impact = sempang
        note = sempang
        masukpengkalandata()

    elif entry.startswith("l"):
        hiasan = "\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}"
        week = sempang
        duration = sempang
        form = semua
        subtheme = raw_input("Enter NAME OF LONG HOLIDAY: \n")
        theme = hiasan + " " + subtheme + " " + hiasan
        topic = sempang
        startdate = raw_input("Enter START DATE: (MMDD)\n")
        lo1 = tahunini+startdate
        enddate = raw_input("Enter END DATE: (MMDD)\n")
        lo2 = tahunini+enddate
        lo3 = sempang
        level = sempang
        content = sempang
        activity1 = sempang
        activity2 = sempang
        assimilation = sempang
        impact = sempang
        note = sempang
        masukpengkalandata()

    elif entry.startswith("o"):
        week = raw_input("Enter WEEK: \n")
        subtheme = raw_input("Enter OFFICIAL EXTERNAL ASSIGNMENT: \n")
        dash = "---"
        theme = dash + " " + subtheme + " " + dash
        subtheme.replace("'","''")
        topic = raw_input("Enter VENUE: \n")
        topic.replace("'","''")
        duration = sempang
        lo1 = sempang
        lo2 = sempang
        form = semua
        level = sempang
        lo3 = sempang
        content = sempang
        activity1 = sempang
        activity2 = sempang
        assimilation = sempang
        impact = sempang
        note = sempang
        masukpengkalandata()

    elif entry.startswith("s"):
        week = raw_input("Enter WEEK: \n")
        subtheme = raw_input("Enter SPECIAL EVENT: \n")
        subtheme.replace("'","''")
        star = "***"
        theme = star + " " + subtheme + " " + star
        print theme
        topic = raw_input("Enter THEME / ANNIVERSARY\n")
        topic.replace("'","''")
        duration = sempang
        lo1 = sempang
        lo2 = sempang
        lo3 = sempang
        form = semua
        level = sempang
        content = sempang
        activity1 = sempang
        activity2 = sempang
        assimilation = sempang
        impact = sempang
        note = sempang
        masukpengkalandata()

    elif entry.startswith("x"):
        week = raw_input("Enter WEEK: \n")
        subtheme = "EXTRA CLASS"
        dash = "+++"
        theme = dash + " " + subtheme + " " + dash
        subtheme.replace("'","''")
        topic = raw_input("Enter TOPIC: \n")
        topic.replace("'","''")
        duration = raw_input("Enter DURATION: \n")
        lo1 = sempang
        lo2 = sempang
        form = semua
        level = sempang
        lo3 = sempang
        content = sempang
        activity1 = sempang
        activity2 = sempang
        assimilation = sempang
        impact = sempang
        note = sempang
        masukpengkalandata()

    else:
        form = raw_input("Enter CLASS: \n")
        level = raw_input("Enter LEVEL: \n")
        if level == "":
            level = "average"
        print level

        week = raw_input("\nEnter WEEK: \n")
        duration = raw_input("Enter DURATION: \n")
        theme = raw_input("Enter THEME: \n")
        topic = raw_input("Enter TOPIC: \n")
        lo1 = raw_input("Enter LEARNING OBJECTIVE 1: \n")

        lo2 = raw_input("Enter LEARNING OBJECTIVE 2: \n")
        if lo2 == "":
            lo2 = "-"
        else:
            lo2.replace("'","''")
        print lo2

        lo3 = raw_input("Enter LEARNING OBJECTIVE 3: \n")
        if lo3 == "":
            lo3 = "-"
        lo3.replace("'","''")
        print lo3

        content = raw_input("Enter CONTENT: \n")
        content.replace("'","''")

        activity1 = raw_input("Enter ACTIVITY 1: \n")
        activity1.replace("'","''")
        print activity1

        activity2 = raw_input("Enter ACTIVITY 2: \n")
        if activity2 == "":
            activity2 = "-"
        activity2.replace("'","''")
        print activity2

        assimilation = raw_input("Enter ASSIMILATION: \n\
                             1-Making Connection\n\
                             2-Making Generalisations\n\
                             3-Making inferences\n\
                             4-Making Interpretations\n\
                             5-Making Associations\n\
                             6-Making Summaries\n\
                             7-Making Conclusions\n\
                             8-Making Decisions\n\
                             9-Identifying and Giving Causes\n\
                             10-Identifying Main Ideas/Supporting Ideas\n\
                             11-Identifying Causes and Effects\n")
        if assimilation == "1":
            assimilation = "Making Connection"
        elif assimilation == "2":
            assimilation = "Making Generalisations"
        elif assimilation == "3":
            assimilation = "Making inferences"
        elif assimilation == "4":
            assimilation = "Making Interpretations"
        elif assimilation == "5":
            assimilation = "Making Associations"
        elif assimilation == "6":
            assimilation = "Making Summaries"
        elif assimilation == "7":
            assimilation = "Making Conclusions"
        elif assimilation == "8":
            assimilation = "Making Decisions"
        elif assimilation == "9":
            assimilation = "Identifying and Giving Causes"
        elif assimilation == "10":
            assimilation = "Identifying Main Ideas/Supporting Ideas"
        elif assimilation == "11":
            assimilation = "Identifying Causes and Effects"
        else:
            assimilation = "-"
        assimilation.replace("'","''")
        print assimilation

        impact = raw_input("Enter IMPACT: \n")
        if impact == "":
            impact = "-"
        impact.replace("'","''")
        print impact

        note = raw_input("Enter NOTE: \n")
        if note == "":
            note = "-"
        note.replace("'","''")
        print note
        masukpengkalandata()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def masuknota():
    print "Masuk Nota\n"
    nota = raw_input("Masukkan nota dalam LP 2015: \n")
    u = Lessonplan2015.select().where(Lessonplan2015.note ==\
                                  '-').order_by(Lessonplan2015.date)
    for i in u:
        print i.id, i.date, i.tingkatan, i.timestart, i.theme, i.topic

    selectlpid = raw_input("Masukkan no LP 2015\n: ")
    query = Lessonplan2015.update(\
                note=nota).\
               where(Lessonplan2015.id == selectlpid)
    query.execute()
    n = Lessonplan2015.select().where(Lessonplan2015.id == selectlpid)
    for a in n:
        print a.date, a.tingkatan, a.theme, a.topic, a.note
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# View Date
def viewdate():
    print "Menu 3\n"
    tarikh = raw_input("Masukkan tarikh [MMDD]\n")
    if tarikh == "":
        hb =  hariini.strftime("%Y%m%d")
    else:
        hb = str(tahunini)+str(tarikh)
    
    u = Lessonplan2015.select().where(Lessonplan2015.date ==\
                                  hb).order_by(Lessonplan2015.timestart)

    print "="*40
    for i in u:
        print i.id, i.tingkatan+" : "+i.timestart+"-"+i.timeend+" Theme: "+i.theme+"\
            Topic:"+i.topic+"Note: "+i.note
    print "="*40
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# View Week

def viewweek():
    print "Menu 3\n"
    week = raw_input("Masukkan no minggu [MM]\n")
    u = Lessonplan2015.select().where(Lessonplan2015.week ==\
                                  week).order_by(Lessonplan2015.date)

    print "="*40
    for i in u:
        print str(i.date)+" : "+i.tingkatan+" : "+i.timestart, i.timeend
    print "="*40
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

#-----------------------------------------------------------------------    

def searchbanktheme():
    print "Cari tema daripada bank\n"
    tema = raw_input("Masukkan tema: \n")
    u = Lessonplanbank.select().where(Lessonplanbank.theme.contains(tema))
    for i in u:
        print "("+str(i.bank)+")\t"+"Form: "+i.tingkatan+":"+i.theme+" : "+i.content
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def searchbanktopic():
    print "Cari topik daripada bank\n"
    topik = raw_input("Masukkan topik: \n")
    u = Lessonplanbank.select().where(Lessonplanbank.topic.contains(topik))
    for i in u:
        print "("+str(i.bank)+")\t"+"Form: "+i.tingkatan+":"+i.topic+" : "+i.content
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def searchlptheme():
    print "Cari tema daripada lp\n"
    tema = raw_input("Masukkan tema: \n")
    u = Lessonplan2015.select().where(Lessonplan2015.theme.contains(tema))
    for i in u:
        print "("+str(i.date)+")\t"+"Form: "+i.tingkatan+":"+i.theme+" : "+i.content
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def searchlptopic():
    print "Cari topik daripada lp\n"
    topik = raw_input("Masukkan topik: \n")
    u = Lessonplan2015.select().where(Lessonplan2015.topic.contains(topik))
    for i in u:
        print "("+str(i.date)+")\t"+"Form: "+i.tingkatan+":"+i.topic+" : "+i.content
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def pindahbankkelp2015():
    selectid = raw_input("\nPlease enter LP BANK ID\n")

    lp = Lessonplan2015.select().where(Lessonplan2015.theme == '-').\
            order_by(Lessonplan2015.timestart).\
            order_by(Lessonplan2015.date)
    for l in lp:
        print "("+str(l.id)+")", str(l.date)+" : "+ l.tingkatan, l.timestart,\
        l.timeend+" ["+l.duration+" minutes] "

    selectlpid = raw_input("\nPlease enter LP 2015 ID\n")

    stok = Lessonplanbank.select().where(Lessonplanbank.bank == selectid)
    for i in stok:
        query = Lessonplan2015.update(\
                duration=i.duration,\
                theme=i.theme,\
                topic=i.topic,\
                lo1=i.lo1,\
                lo2=i.lo2,\
                lo3=i.lo3,\
                content=i.content,\
                activity1=i.activity1,\
                activity2=i.activity2,\
                assimilation=i.assimilation).\
               where(Lessonplan2015.id == selectlpid)
        query.execute()

    lp2015baru = Lessonplan2015.select().where(Lessonplan2015.id == selectlpid)

    print ""
    print "=" * 60
    for j in lp2015baru:
        print "["+str(j.date)+"]", j.tingkatan
        print "\t "+str(j.timestart)+" -- "+str(j.timeend)
        print "\t LO1: "+j.lo1
        print "\t LO2: "+j.lo2
        print "\t Content: "+j.content
        print "\t Activity 1 :"+str(j.activity1)
        print "\t Activity 2 :"+str(j.activity2)
    print "=" * 60
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def deletelp2015id():
    lpid = raw_input("Masukkan id Lesson 2015 LP: \n")
    query = Lessonplan2015.delete().where(Lessonplan2015.id == lpid)
    query.execute()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def pindahbankkelp2015tarikh ():
    selectid = raw_input("\nPlease enter LP BANK ID\n")

    lp = Lessonplan2015.select().where(Lessonplan2015.theme == '-').\
            order_by(Lessonplan2015.timestart).\
            order_by(Lessonplan2015.date)
    for l in lp:
        print "("+str(l.id)+")", str(l.date)+" : "+ l.tingkatan, l.timestart,\
        l.timeend+" ["+l.duration+" minutes] "

    selectlpid = raw_input("\nPlease enter LP 2015 date\n")

    stok = Lessonplanbank.select().where(Lessonplanbank.bank == selectid)
    for i in stok:
        query = Lessonplan2015.update(\
                duration=i.duration,\
                theme=i.theme,\
                topic=i.topic,\
                lo1=i.lo1,\
                lo2=i.lo2,\
                lo3=i.lo3,\
                content=i.content,\
                activity1=i.activity1,\
                activity2=i.activity2,\
                assimilation=i.assimilation).\
               where(Lessonplan2015.date == selectlpid)
        query.execute()

    lp2015baru = Lessonplan2015.select().where(Lessonplan2015.date == selectlpid)

    print ""
    print "=" * 60
    for j in lp2015baru:
        print "["+str(j.date)+"]", j.tingkatan
        print "\t "+str(j.timestart)+" -- "+str(j.timeend)
        print "\t LO1: "+j.lo1
        print "\t LO2: "+j.lo2
        print "\t Content: "+j.content
        print "\t Activity 1 :"+str(j.activity1)
        print "\t Activity 2 :"+str(j.activity2)
    print "=" * 60
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def hantarsalinan():
    with open(backupdir+'dump-lp2015-'+harini+'.sql', 'rb') as f_in, gzip.open(backupdir+'dump-lp2015-'+harini+'.sql.gz', 'wb') as f_out :
        shutil.copyfileobj(f_in, f_out)
    print "="*20
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


def calendarview():
    bulan = raw_input("\nMasukkan bulan [MM]: \n")
    tahunini = int(datetime.datetime.now().year)
    calendar.prmonth(tahunini, int(bulan))
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def writeweekly():
    week = raw_input("Masukkan nombor minggu: \n")

    lpweeksun = Lessonplan2015.get(Lessonplan2015.week == week)

    datesun = int(lpweeksun.date)

    #sdir = "/tmp/"
    sdir = "/storage/extSdCard/lp2015/"

    failtex = sdir+"weekly-week-"+str(week)+"-"+str(datesun)+".tex"
    failtexlog = sdir+"weekly"+str(datesun)+".log"
    failtexaux = sdir+"weekly"+str(datesun)+".aux"
    failtexpdf = sdir+"weekly"+str(datesun)+".pdf"
    failkeluar = open(failtex, "w")  

    tdatemon = datetime.datetime.strptime(str(datesun), '%Y%m%d') + datetime.timedelta(days=1)
    tdatetue = datetime.datetime.strptime(str(datesun), '%Y%m%d') + datetime.timedelta(days=2)
    tdatewed = datetime.datetime.strptime(str(datesun), '%Y%m%d') + datetime.timedelta(days=3)
    tdatethu = datetime.datetime.strptime(str(datesun), '%Y%m%d') + datetime.timedelta(days=4)

    datemon = tdatemon.strftime('%Y%m%d')
    datetue = tdatetue.strftime('%Y%m%d')
    datewed = tdatewed.strftime('%Y%m%d')
    datethu = tdatethu.strftime('%Y%m%d')                             

    print datesun

    print >>failkeluar,"\\documentclass[a4paper,12pt]{article}\n\
    \\usepackage{palatino}\n\
    \\usepackage{fancyvrb,pifont,enumerate,url,graphicx,tabularx,longtable,quotes,setspace,floatflt,umoline,rotating,soul}\n\
    \\usepackage[top=1.8cm,bottom=2cm,left=1.5cm,right=1.5cm]{geometry}\n\
    \\usepackage{fancyhdr} \\pagestyle{fancy}\n"
    print >>failkeluar,"\\usepackage{nopageno}"

    print >>failkeluar,"\\usepackage{onepagem}\n\
    \\usepackage{pstricks}\n\
    \\setlength\\parindent{0pt}\n\
    \\begin{document}\n"

    namahari = time.strftime("%A",time.strptime(str(datesun),"%Y%m%d"))
    tarikh_dalam_perkataan = time.strftime("%d %B %Y",time.strptime(str(datesun),"%Y%m%d"))

    print >>failkeluar,"%s \\hspace{7cm} Week %s \\hfill %s"  % (namahari, week,tarikh_dalam_perkataan)

    print >>failkeluar,"\\begin{longtable}{|p{2.3cm}|p{3.9cm}p{0.3cm}p{9.8cm}|}\\hline\n\
    \\centerline{TIME/CLASS}&\\multicolumn{3}{c|}{\\textit{TOPIC / LEARNING\
    OUTCOME / CONTENT / ACTIVITIES /}}\\\\\n\
    \n\\centerline{SUBJECT}&\\multicolumn{3}{c|}{\\textit{ASSIMILATION /\
    EVALUATION}}\\\\\n\
    &&&\\\\\n\
    \\hline"

    weeksun = Lessonplan2015.select().where(Lessonplan2015.date == datesun)

    for i in weeksun:

        if i.theme.startswith("PEPERIKSAAN"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{%s}   \\\\" % (i.timestart,i.timeend,i.theme.upper())
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\ \
            &&&\\\\" % i.topic 
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{[%s]}} \\\\" % i.lo1
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" %  i.lo2
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" % i.lo3
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline"

        elif 'Cuti' in i.theme:
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n &  \\multicolumn{3}{c|}{\\so{%s}}\
            \\\\" % theme
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\"\
            % i.topic
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" %\
            i.lo1
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" % i.lo2
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" % i.lo3
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&&   \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith("***"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{}   \\\\" % (i.timestart,i.timeend) 
            theme = i.theme.upper()
            print >>failkeluar,"\n &  \\multicolumn{3}{c|}{%s}\
            \\\\" % i.theme
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" %\
            i.topic
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}} \\\\" % i.lo1
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}} \\\\" % i.lo2
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline \n"

        elif i.theme.startswith('---'):
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{%s}\
            \\\\" % theme
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}} \\\\" %\
            i.topic
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith('+++'):
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak & \
            \\multicolumn{3}{c|}{%s}\\\\"  % (i.tingkatan,theme)
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{%s}   \\\\" % (i.timestart,i.timeend,i.topic)
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith("\ding{90}"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{{\\textcolor{blue}{%s}}}\
            \\\\" % i.theme
            print >>failkeluar,"&&&\\\\"
            tarikh_akhir_cuti_dalam_perkataan =  time.strftime("%d %B %Y",time.strptime(lo2,"%Y%m%d"))
            print >>failkeluar," & \\multicolumn{3}{c|}{{%s ---- %s}}\\\\" %\
            (tarikh_dalam_perkataan,tarikh_akhir_cuti_dalam_perkataan)
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&\\multicolumn{3}{c|}{\\textcolor{blue}{\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}}}\\\\"
            print >>failkeluar,"\\hline\n"

        else:
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\\n"
            print >>failkeluar,"\\centerline{%s-%s}&Theme / Topic&:& %s -\
            \\textit{%s}\\\\" %  (i.timestart,i.timeend,i.theme,i.topic)
            print >>failkeluar,"\\centerline{English}&Learning\
            objective(s)&:&Students will be able to:\\\\"
            print >>failkeluar,"&&&(i) %s\\\\\n" % i.lo1
            print >>failkeluar,"&&&(ii) %s\\\\\n" % i.lo2
            print >>failkeluar,"&&&(iii) %s\\\\\n" % i.lo3
            print >>failkeluar,"&Content&:& %s\\\\\n" % i.content
            print >>failkeluar,"&Activities&:& \\ding{172} %s, \\ding{173}\
            %s\\\\\n" % (i.activity1,i.activity2)
            print >>failkeluar,"&Assimilation&:& %s\\\\" % i.assimilation
            print >>failkeluar,"&Impact/Reflection&:& \\textit{%s}\\\\\n" % i.impact
            print >>failkeluar,"\\hline\n"

    print >>failkeluar,"\\end{longtable}\n"


    print >>failkeluar,"\\vfill"

    print\
    >>failkeluar,".........................................\\hspace{8.8cm}Tarikh/\\textit{Date}.........................\n"

    print >>failkeluar,"Tandatangan Pengetua\n"
    print >>failkeluar,"\\textit{Principal's Signature}"

    print >>failkeluar,"\\newpage"


    weekmon = Lessonplan2015.select().where(Lessonplan2015.date == datemon)

    namahari = time.strftime("%A",time.strptime(str(datemon),"%Y%m%d"))
    tarikh_dalam_perkataan = time.strftime("%d %B %Y",time.strptime(str(datemon),"%Y%m%d"))

    print >>failkeluar,"%s \\hspace{7cm} Week %s \\hfill %s"  % (namahari, week,tarikh_dalam_perkataan)


    print >>failkeluar,"\\begin{longtable}{|p{2.3cm}|p{3.9cm}p{0.3cm}p{9.8cm}|}\\hline\n\
    \\centerline{TIME/CLASS}&\\multicolumn{3}{c|}{\\textit{TOPIC / LEARNING\
	OUTCOME / CONTENT / ACTIVITIES /}}\\\\\n\
	\n\\centerline{SUBJECT}&\\multicolumn{3}{c|}{\\textit{ASSIMILATION /\
	EVALUATION}}\\\\\n\
	&&&\\\\\n\
	\\hline"



    for i in weekmon:

        if i.theme.startswith("PEPERIKSAAN"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{%s}   \\\\" % (i.timestart,i.timeend,i.theme.upper())
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\ \
            &&&\\\\" % i.topic 
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{[%s]}} \\\\" % i.lo1
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" %  i.lo2
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" % i.lo3
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline"

        elif 'Cuti' in i.theme:
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n &  \\multicolumn{3}{c|}{%s}\
            \\\\" % theme
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\"\
            % i.topic
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" %\
            i.lo1
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" % i.lo2
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" % i.lo3
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&&   \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith("***"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{}   \\\\" % (i.timestart,i.timeend) 
            theme = i.theme.upper()
            print >>failkeluar,"\n &  \\multicolumn{3}{c|}{%s}\
            \\\\" % i.theme
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" %\
            i.topic
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}} \\\\" % i.lo1
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}} \\\\" % i.lo2
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline \n"

        elif i.theme.startswith('---'):
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{%s}\
            \\\\" % theme
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}} \\\\" %\
            i.topic
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith('+++'):
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak & \
            \\multicolumn{3}{c|}{%s}\\\\"  % (i.tingkatan,theme)
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{%s}   \\\\" % (i.timestart,i.timeend,i.topic)
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith("\ding{90}"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{{\\textcolor{blue}{%s}}}\
            \\\\" % i.theme
            print >>failkeluar,"&&&\\\\"
            tarikh_akhir_cuti_dalam_perkataan =  time.strftime("%d %B %Y",time.strptime(lo2,"%Y%m%d"))
            print >>failkeluar," & \\multicolumn{3}{c|}{{%s ---- %s}}\\\\" %\
            (tarikh_dalam_perkataan,tarikh_akhir_cuti_dalam_perkataan)
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&\\multicolumn{3}{c|}{\\textcolor{blue}{\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}}}\\\\"
            print >>failkeluar,"\\hline\n"

        else:
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\\n"
            print >>failkeluar,"\\centerline{%s-%s}&Theme / Topic&:& %s -\
            \\textit{%s}\\\\" %  (i.timestart,i.timeend,i.theme,i.topic)
            print >>failkeluar,"\\centerline{English}&Learning\
            objective(s)&:&Students will be able to:\\\\"
            print >>failkeluar,"&&&(i) %s\\\\\n" % i.lo1
            print >>failkeluar,"&&&(ii) %s\\\\\n" % i.lo2
            print >>failkeluar,"&&&(iii) %s\\\\\n" % i.lo3
            print >>failkeluar,"&Content&:& %s\\\\\n" % i.content
            print >>failkeluar,"&Activities&:& \\ding{172} %s, \\ding{173}\
            %s\\\\\n" % (i.activity1,i.activity2)
            print >>failkeluar,"&Assimilation&:& %s\\\\" % i.assimilation
            print >>failkeluar,"&Impact/Reflection&:& \\textit{%s}\\\\\n" % i.impact
            print >>failkeluar,"\\hline\n"

    print >>failkeluar,"\\end{longtable}\n"


    print >>failkeluar,"\\vfill"

    print\
    >>failkeluar,".........................................\\hspace{8.8cm}Tarikh/\\textit{Date}.........................\n"

    print >>failkeluar,"Tandatangan Pengetua\n"
    print >>failkeluar,"\\textit{Principal's Signature}"



    print >>failkeluar,"\\newpage"

    weektue = Lessonplan2015.select().where(Lessonplan2015.date == datetue)
    namahari = time.strftime("%A",time.strptime(str(datetue),"%Y%m%d"))
    tarikh_dalam_perkataan = time.strftime("%d %B %Y",time.strptime(str(datetue),"%Y%m%d"))

    print >>failkeluar,"%s \\hspace{7cm} Week %s \\hfill %s"  % (namahari, week,tarikh_dalam_perkataan)

    print >>failkeluar,"\\begin{longtable}{|p{2.3cm}|p{3.9cm}p{0.3cm}p{9.8cm}|}\\hline\n\
    \\centerline{TIME/CLASS}&\\multicolumn{3}{c|}{\\textit{TOPIC / LEARNING\
    OUTCOME / CONTENT / ACTIVITIES /}}\\\\\n\
    \n\\centerline{SUBJECT}&\\multicolumn{3}{c|}{\\textit{ASSIMILATION /\
    EVALUATION}}\\\\\n\
    &&&\\\\\n\
    \\hline"


    for i in weektue:
        if i.theme.startswith("PEPERIKSAAN"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{%s}   \\\\" % (i.timestart,i.timeend,i.theme.upper())
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\ \
            &&&\\\\" % i.topic 
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{[%s]}} \\\\" % i.lo1
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" %  i.lo2
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" % i.lo3
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline"

        elif 'Cuti' in i.theme:
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n &  \\multicolumn{3}{c|}{%s}\
            \\\\" % theme
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\"\
            % i.topic
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" %\
            i.lo1
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" % i.lo2
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" % i.lo3
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&&   \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith("***"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{}   \\\\" % (i.timestart,i.timeend) 
            theme = i.theme.upper()
            print >>failkeluar,"\n &  \\multicolumn{3}{c|}{%s}\
            \\\\" % i.theme
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" %\
            i.topic
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}} \\\\" % i.lo1
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}} \\\\" % i.lo2
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline \n"

        elif i.theme.startswith('---'):
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{%s}\
            \\\\" % theme
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}} \\\\" %\
            i.topic
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith('+++'):
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak & \
            \\multicolumn{3}{c|}{%s}\\\\"  % (i.tingkatan,theme)
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{%s}   \\\\" % (i.timestart,i.timeend,i.topic)
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith("\ding{90}"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{{\\textcolor{blue}{%s}}}\
            \\\\" % i.theme
            print >>failkeluar,"&&&\\\\"
            tarikh_akhir_cuti_dalam_perkataan =  time.strftime("%d %B %Y",time.strptime(lo2,"%Y%m%d"))
            print >>failkeluar," & \\multicolumn{3}{c|}{{%s ---- %s}}\\\\" %\
            (tarikh_dalam_perkataan,tarikh_akhir_cuti_dalam_perkataan)
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&\\multicolumn{3}{c|}{\\textcolor{blue}{\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}}}\\\\"
            print >>failkeluar,"\\hline\n"

        else:
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\\n"
            print >>failkeluar,"\\centerline{%s-%s}&Theme / Topic&:& %s -\
            \\textit{%s}\\\\" %  (i.timestart,i.timeend,i.theme,i.topic)
            print >>failkeluar,"\\centerline{English}&Learning\
            objective(s)&:&Students will be able to:\\\\"
            print >>failkeluar,"&&&(i) %s\\\\\n" % i.lo1
            print >>failkeluar,"&&&(ii) %s\\\\\n" % i.lo2
            print >>failkeluar,"&&&(iii) %s\\\\\n" % i.lo3
            print >>failkeluar,"&Content&:& %s\\\\\n" % i.content
            print >>failkeluar,"&Activities&:& \\ding{172} %s, \\ding{173}\
            %s\\\\\n" % (i.activity1,i.activity2)
            print >>failkeluar,"&Assimilation&:& %s\\\\" % i.assimilation
            print >>failkeluar,"&Impact/Reflection&:& \\textit{%s}\\\\\n" % i.impact
            print >>failkeluar,"\\hline\n"

    print >>failkeluar,"\\end{longtable}\n"
    print >>failkeluar,"\\vfill"

    print\
    >>failkeluar,".........................................\\hspace{8.8cm}Tarikh/\\textit{Date}.........................\n"

    print >>failkeluar,"Tandatangan Pengetua\n"
    print >>failkeluar,"\\textit{Principal's Signature}"

    print >>failkeluar,"\\newpage"

    weekwed = Lessonplan2015.select().where(Lessonplan2015.date == datewed)

    namahari = time.strftime("%A",time.strptime(str(datewed),"%Y%m%d"))
    tarikh_dalam_perkataan = time.strftime("%d %B %Y",time.strptime(str(datewed),"%Y%m%d"))

    print >>failkeluar,"%s \\hspace{7cm} Week %s \\hfill %s"  % (namahari, week,tarikh_dalam_perkataan)

    print >>failkeluar,"\\begin{longtable}{|p{2.3cm}|p{3.9cm}p{0.3cm}p{9.8cm}|}\\hline\n\
    \\centerline{TIME/CLASS}&\\multicolumn{3}{c|}{\\textit{TOPIC / LEARNING\
    OUTCOME / CONTENT / ACTIVITIES /}}\\\\\n\
    \n\\centerline{SUBJECT}&\\multicolumn{3}{c|}{\\textit{ASSIMILATION /\
    EVALUATION}}\\\\\n\
    &&&\\\\\n\
    \\hline"

    for i in weekwed:

        if i.theme.startswith("PEPERIKSAAN"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{%s}   \\\\" % (i.timestart,i.timeend,i.theme.upper())
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\ \
            &&&\\\\" % i.topic 
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{[%s]}} \\\\" % i.lo1
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" %  i.lo2
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" % i.lo3
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline"

        elif 'Cuti' in i.theme:
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n &  \\multicolumn{3}{c|}{%s}\
            \\\\" % theme
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\"\
            % i.topic
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" %\
            i.lo1
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" % i.lo2
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" % i.lo3
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&&   \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith("***"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{}   \\\\" % (i.timestart,i.timeend) 
            theme = i.theme.upper()
            print >>failkeluar,"\n &  \\multicolumn{3}{c|}{%s}\
            \\\\" % i.theme
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" %\
            i.topic
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}} \\\\" % i.lo1
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}} \\\\" % i.lo2
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline \n"

        elif i.theme.startswith('---'):
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{%s}\
            \\\\" % theme
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}} \\\\" %\
            i.topic
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith('+++'):
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak & \
            \\multicolumn{3}{c|}{%s}\\\\"  % (i.tingkatan,theme)
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{%s}   \\\\" % (i.timestart,i.timeend,i.topic)
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith("\ding{90}"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{{\\textcolor{blue}{%s}}}\
            \\\\" % i.theme
            print >>failkeluar,"&&&\\\\"
            tarikh_akhir_cuti_dalam_perkataan =  time.strftime("%d %B %Y",time.strptime(lo2,"%Y%m%d"))
            print >>failkeluar," & \\multicolumn{3}{c|}{{%s ---- %s}}\\\\" %\
            (tarikh_dalam_perkataan,tarikh_akhir_cuti_dalam_perkataan)
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&\\multicolumn{3}{c|}{\\textcolor{blue}{\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}}}\\\\"
            print >>failkeluar,"\\hline\n"

        else:
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\\n"
            print >>failkeluar,"\\centerline{%s-%s}&Theme / Topic&:& %s -\
            \\textit{%s}\\\\" %  (i.timestart,i.timeend,i.theme,i.topic)
            print >>failkeluar,"\\centerline{English}&Learning\
            objective(s)&:&Students will be able to:\\\\"
            print >>failkeluar,"&&&(i) %s\\\\\n" % i.lo1
            print >>failkeluar,"&&&(ii) %s\\\\\n" % i.lo2
            print >>failkeluar,"&&&(iii) %s\\\\\n" % i.lo3
            print >>failkeluar,"&Content&:& %s\\\\\n" % i.content
            print >>failkeluar,"&Activities&:& \\ding{172} %s, \\ding{173}\
            %s\\\\\n" % (i.activity1,i.activity2)
            print >>failkeluar,"&Assimilation&:& %s\\\\" % i.assimilation
            print >>failkeluar,"&Impact/Reflection&:& \\textit{%s}\\\\\n" % i.impact
            print >>failkeluar,"\\hline\n"

    print >>failkeluar,"\\end{longtable}\n"


    print >>failkeluar,"\\vfill"

    print\
    >>failkeluar,".........................................\\hspace{8.8cm}Tarikh/\\textit{Date}.........................\n"

    print >>failkeluar,"Tandatangan Pengetua\n"
    print >>failkeluar,"\\textit{Principal's Signature}"

    print >>failkeluar,"\\newpage"

    weekthu = Lessonplan2015.select().where(Lessonplan2015.date == datethu)

    namahari = time.strftime("%A",time.strptime(str(datethu),"%Y%m%d"))
    tarikh_dalam_perkataan = time.strftime("%d %B %Y",time.strptime(str(datethu),"%Y%m%d"))

    print >>failkeluar,"%s \\hspace{7cm} Week %s \\hfill %s"  % (namahari, week,tarikh_dalam_perkataan)

    print >>failkeluar,"\\begin{longtable}{|p{2.3cm}|p{3.9cm}p{0.3cm}p{9.8cm}|}\\hline\n\
    \\centerline{TIME/CLASS}&\\multicolumn{3}{c|}{\\textit{TOPIC / LEARNING\
    OUTCOME / CONTENT / ACTIVITIES /}}\\\\\n\
    \n\\centerline{SUBJECT}&\\multicolumn{3}{c|}{\\textit{ASSIMILATION /\
    EVALUATION}}\\\\\n\
    &&&\\\\\n\
    \\hline"

    for i in weekthu:

        if i.theme.startswith("PEPERIKSAAN"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{%s}   \\\\" % (i.timestart,i.timeend,i.theme.upper())
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\ \
            &&&\\\\" % i.topic 
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{[%s]}} \\\\" % i.lo1
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" %  i.lo2
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" % i.lo3
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline"

        elif 'Cuti' in i.theme:
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n &  \\multicolumn{3}{c|}{%s}\
            \\\\" % theme
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}  \\\\"\
            % i.topic
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" %\
            i.lo1
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" % i.lo2
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}}\\\\" % i.lo3
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&&   \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith("***"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{}   \\\\" % (i.timestart,i.timeend) 
            theme = i.theme.upper()
            print >>failkeluar,"\n &  \\multicolumn{3}{c|}{%s}\
            \\\\" % i.theme
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}}  \\\\" %\
            i.topic
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}} \\\\" % i.lo1
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{\\textit{%s}} \\\\" % i.lo2
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"&&& \\\\"
            print >>failkeluar,"\\hline \n"

        elif i.theme.startswith('---'):
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{%s}\
            \\\\" % theme
            print >>failkeluar,"\n& \\multicolumn{3}{c|}{\\textit{%s}} \\\\" %\
            i.topic
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith('+++'):
            theme = i.theme.upper()
            print >>failkeluar,"\\centerline{%s}\\linebreak & \
            \\multicolumn{3}{c|}{%s}\\\\"  % (i.tingkatan,theme)
            print >>failkeluar,"\n\\centerline{%s-%s}&\
            \\multicolumn{3}{c|}{%s}   \\\\" % (i.timestart,i.timeend,i.topic)
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\\hline\n"

        elif i.theme.startswith("\ding{90}"):
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"\n & \\multicolumn{3}{c|}{{\\textcolor{blue}{%s}}}\
            \\\\" % i.theme
            print >>failkeluar,"&&&\\\\"
            tarikh_akhir_cuti_dalam_perkataan =  time.strftime("%d %B %Y",time.strptime(lo2,"%Y%m%d"))
            print >>failkeluar," & \\multicolumn{3}{c|}{{%s ---- %s}}\\\\" %\
            (tarikh_dalam_perkataan,tarikh_akhir_cuti_dalam_perkataan)
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&&&\\\\"
            print >>failkeluar,"&\\multicolumn{3}{c|}{\\textcolor{blue}{\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}\ding{90}}}\\\\"
            print >>failkeluar,"\\hline\n"

        else:
            print >>failkeluar,"\\centerline{%s}\\linebreak" % i.tingkatan
            print >>failkeluar,"&&&\\\\\n"
            print >>failkeluar,"\\centerline{%s-%s}&Theme / Topic&:& %s -\
            \\textit{%s}\\\\" %  (i.timestart,i.timeend,i.theme,i.topic)
            print >>failkeluar,"\\centerline{English}&Learning\
            objective(s)&:&Students will be able to:\\\\"
            print >>failkeluar,"&&&(i) %s\\\\\n" % i.lo1
            print >>failkeluar,"&&&(ii) %s\\\\\n" % i.lo2
            print >>failkeluar,"&&&(iii) %s\\\\\n" % i.lo3
            print >>failkeluar,"&Content&:& %s\\\\\n" % i.content
            print >>failkeluar,"&Activities&:& \\ding{172} %s, \\ding{173}\
            %s\\\\\n" % (i.activity1,i.activity2)
            print >>failkeluar,"&Assimilation&:& %s\\\\" % i.assimilation
            print >>failkeluar,"&Impact/Reflection&:& \\textit{%s}\\\\\n" % i.impact
            print >>failkeluar,"\\hline\n"

    print >>failkeluar,"\\end{longtable}\n"

    print >>failkeluar,"\\vfill"

    print\
>>failkeluar,".........................................\\hspace{8.8cm}Tarikh/\\textit{Date}.........................\n"

    print >>failkeluar,"Tandatangan Pengetua\n"
    print >>failkeluar,"\\textit{Principal's Signature}"

    print >>failkeluar,"\\end{document}\n"

    failkeluar.close()
    print "9. Kembali"
    print "0. Keluar"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return 

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    'bu': peliharadata,
    'cv': calendarview,
    'dl': deletelp2015id,
    'hs': hantarsalinan,
    'mb': masuklessonplanbank,
    'mn': masuknota,
    'pl': pindahbankkelp2015,
    'pt': pindahbankkelp2015tarikh,
    'vw': viewweek,
    'vd': viewdate,
    'sbto': searchbanktopic,
    'sbth': searchbanktheme,
    'slto': searchlptopic,
    'slth': searchlptheme,
    'ww': writeweekly,
    '9': back,
    'q': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
