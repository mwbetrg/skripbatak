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

import re
import site
import sys, os
import datetime
import time
import calendar
import smtplib
import getpass
import sqlite3

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import ConfigParser
from peewee import *


#-----------------------------------------------------------------------    

if os.path.exists('/storage/extSdCard'):
    database = SqliteDatabase('/storage/extSdCard/mydb/english-notes-exercises.sqlite', **{})
    backupdir = '/storage/extSdCard/dbbackup/'
    db = '/storage/extSdCard/mydb/english-notes-exercises.sqlite'
else:
    database = SqliteDatabase('english-notes-exercises.sqlite', **{})

class BaseModel(Model):
    class Meta:
        database = database

class Iotd(BaseModel):
    date = TextField(null=True)
    id = IntegerField(null=True)  # integer primarykey
    idiom = TextField(unique=True)
    meaning = TextField(null=True)
    sentence = TextField(null=True)

    class Meta:
        db_table = 'iotd'

class Questionsmaster(BaseModel):
    cat = TextField(null=True)
    instructions = CharField(null=True)
    level  = TextField(null=True)
    source = TextField(null=True)
    suggestions = CharField(null=True)
    time = TimeField(null=True)
    topic = TextField()
    type = TextField(null=True)

    class Meta:
        db_table = 'questionsmaster'

class Questionsfb(BaseModel):
    answer = TextField(null=True)
    item = TextField(null=True)
    topicid = ForeignKeyField(db_column='topicid', rel_model=Questionsmaster, to_field='id')

    class Meta:
        db_table = 'questionsfb'

class Questionsmcq(BaseModel):
    choicea = TextField(null=True)
    choiceb = TextField(null=True)
    choicec = TextField(null=True)
    choiced = TextField(null=True)
    item = TextField()
    ticka = TextField(null=True)
    tickb = TextField(null=True)
    tickc = TextField(null=True)
    tickd = TextField(null=True)
    topicid = ForeignKeyField(db_column='topicid', null=True, rel_model=Questionsmaster, to_field='id')

    class Meta:
        db_table = 'questionsmcq'


class Totd(BaseModel):
    date = TextField(null=True)
    issue = TextField(unique=True)
    right = TextField(null=True)
    wrong = TextField(null=True)

    class Meta:
        db_table = 'totd'


class Wotd(BaseModel):
    date = TextField(null=True)
    id = IntegerField(null=True)  # integer primarykey
    meaning = TextField(null=True)  # 
    part = TextField(null=True)
    sentence = TextField(null=True)
    word = TextField(unique=True)

    class Meta:
        db_table = 'wotd'


class Muetvocab(BaseModel):
    date = TextField(null=True)
    kata = TextField(null=True)
    part = TextField(null=True)
    sentence = TextField(null=True)
    word = TextField(unique=True)

    class Meta:
        db_table = 'muetvocab'

class Webcontents(BaseModel):
    content = TextField(null=True)
    tags = CharField(null=True)
    time = DateTimeField(null=True)
    url = CharField(null=True)

    class Meta:
        db_table = 'webcontents'



database.connect()

#-----------------------------------------------------------------------    
today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)
esok = tomorrow.strftime("%Y%m%d")
 
tahunini = datetime.datetime.today().year
bulanini = today.strftime("%Y%m")
harini = today.strftime("%Y%m%d")
# Main definition - constants
menu_actions  = {}  

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    
    print ":: English ::\n"
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

# Word for tomorrow
def wordtomorrow():
    print "Word for tomorrow\n"
    w = Wotd.select().where(Wotd.date == esok)
    for i in w:
        print "\n["+i.date+"] "+i.word+" ("+i.meaning+") : "+i.sentence
    print "9. Kembali"
    print "0. Keluar"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Idiom for tomorrow
def idiomtomorrow():
    print "Idiom for tomorrow\n"
    reload(sys) 
    sys.setdefaultencoding('utf8')
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)
    esok = tomorrow.strftime("%Y%m%d")
    w = Iotd.select().where(Iotd.date == esok)
    for i in w:
        print "\n["+i.date+"] "+i.idiom+" ("+i.meaning+") : "+i.sentence+"\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Add word 
def addword():
    print "Word Of The Day"
    kata = raw_input("Enter new word: \n")
    kata = kata.strip().lower()
    jenis = raw_input("Enter the part of speech: \n")
    if jenis == "n" :
        jenis = "noun"
    elif jenis == "v" :
        jenis = "verb" 
    elif jenis == "adj" :
        jenis = "adjective"
    elif jenis == "adv" :
        jenis = "adverb"
    else:
        jenis = jenis
    print jenis 
    makna = raw_input("Enter the meaning: \n")
    makna = makna.strip().lower()
    ayat = raw_input("Enter the sentence [identify textcolor with *word*] :\n")
    ayat = re.sub(r'\*(.*?)\*', r'\\textcolor{blue}{\1}', ayat)
    print '='*30
    print ayat
    print '='*30
    tarikh = raw_input("Enter the date [YYYYMMDD]:\n")
    if tarikh == "":
        hb = bulanini
    else:
        hb = tarikh
    print tarikh
    simpan = Wotd.insert(word=kata, part=jenis, meaning=makna,\
                         date=hb,sentence=ayat).execute()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Add idiom 
def addidiom():
    print "Idiom Of The Day"
    peribahasa = raw_input("Enter new idiom: \n")
    peribahasa = peribahasa.strip().lower()
    makna = raw_input("Enter the meaning: \n")
    makna = makna.strip().lower()
    ayat = raw_input("Enter the sentence [identify textcolor with *word*] :\n")
    ayat = re.sub(r'\*(.*?)\*', r'\\textcolor{blue}{\1}', ayat)
    print '='*30
    print ayat
    print '='*30
    tarikh = raw_input("Enter the date [YYYYMMDD]:\n")
    if tarikh == "":
        hb = bulanini
    else:
        hb = tarikh
    print tarikh
    simpan = Iotd.insert(idiom=peribahasa,  meaning=makna,\
                         date=hb,sentence=ayat).execute()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def addmuet():
    print "MUET Vocab"
    kata = raw_input("Enter new word: \n")
    jenis = raw_input("Enter the part of speech: \n")
    makna = raw_input("Enter the meaning (Malay): \n")
    ayat = raw_input("Enter the sentence [identify textcolor with *word*] :\n")
    ayat = re.sub(r'\*(.*?)\*', r'\\textcolor{blue}{\1}', ayat)
    print '='*len(ayat)
    print ayat
    print '='*len(ayat)
    tarikh = raw_input("Enter the date [YYYYMMDD]:\n")
    if tarikh == "":
        hb = bulanini
    else:
        hb = tarikh
    print tarikh
    simpan = Muetvocab.insert(word=kata, part=jenis, kata=makna,\
                         date=hb,sentence=ayat).execute()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def addtip():
    print "Tip Of The Day"
    issue = raw_input("Enter new issue: \n")
    issue = issue.strip().lower()
    wrong = raw_input("Enter the wrong usage : \n")
    wrong = wrong.strip().lower()
    right = raw_input("Enter the right usage: \n")
    right = right.strip().lower()
    print '='*30
    print wrong
    print right
    print '='*30
    tarikh = raw_input("Enter the date [YYYYMMDD]:\n")
    if tarikh == "":
        hb = bulanini
    else:
        hb = tarikh
    print tarikh
    simpan = Totd.insert(issue=issue, wrong=wrong, right=right,\
                         date=hb).execute()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def searchtip():
    reload(sys) 
    sys.setdefaultencoding('utf8')
    print "Search right usage from Tip\n"
    right = raw_input("Enter right usage: \n")
    u = Totd.select().where(Totd.right.contains(right))
    for i in u:
        print "="*len(i.issue)+"\n"+str(i.wrong)+"\n"+"="*len(i.right)
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def searchweburl():
    reload(sys) 
    sys.setdefaultencoding('utf8')
    print "Search web content\n"
    content = raw_input("Enter content: \n")
    u = Webcontents.select().where(Webcontents.content.contains(content))
    print '='*30
    for i in u:
        print i.content+"\n"+str(i.content)+"\n"
    print "="*30
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Write Word

def writeword():
    tarikh = (time.strftime("%Y%m%d"))
    sdir = "/storage/extSdCard/texdocs/wotd/"
    failtex = sdir+"wotd-"+tarikh+".tex"
    failkeluar = open(failtex, "w")  
    print tarikh
    w = Wotd.select().where(Wotd.date == tarikh)

    print >>failkeluar,"\documentclass[12pt,a5paper]{article}\n\
    \usepackage{palatino}\n\
    \usepackage{nopageno}\n\
    \usepackage{floatflt}\n\
    \usepackage[top=1.5cm,bottom=2cm, left=1.5cm,right=1.5cm]{geometry}\n\
    \usepackage{pdflscape,soul}\n\
    \usepackage{pifont}\n\
    \usepackage{graphicx}\n\
    \usepackage{xcolor}\n\
    \setlength\parindent{0pt}\n\n\
    \\begin{document}\n\n\
    \\begin{landscape}\n\
    \\Huge\n\
    \\centerline{\\textcolor{orange}{\\so{WORD(S) OF THE DAY}}}\n\
    \\medskip\n\
    \\begin{center}\n"
    for i in w:
        print i.word+"\n"+i.meaning+"\n"+i.sentence
        print >>failkeluar,"\\textbf{\\so{%s}} \n\n \\medskip" % i.word
        print >>failkeluar,"\\begin{minipage}{14cm}  \\textcolor{magenta}{[%s]}  \\textit{%s} " \
        %  (i.part, i.meaning)
        print >>failkeluar,"\\end{minipage} \n\n\
        \\medskip \n\
        \\begin{minipage}{14cm}\n\
        \\begin{center}\n"
        print >>failkeluar,"\\texttt{%s}\n\n"   % i.sentence
        print >>failkeluar,"\\end{center} \\end{minipage}\n\n\
        \\vfill\n\n\
        \\includegraphics[scale=0.5]{ornamental-flower-horizontal.jpg} \
        \\includegraphics[scale=0.5]{ornamental-flower-horizontal.jpg}\n\
        \\end{center}\n\n\
        \\end{landscape}\n\n\
        \\end{document}"
    failkeluar.close()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def writeidiom():
    tarikh = (time.strftime("%Y%m%d"))

    failtex = "/storage/extSdCard/texdocs/iotd/iotd-"+tarikh+".tex"
    failkeluar = open(failtex, "w")  
    reload(sys) 
    sys.setdefaultencoding('utf8')
    print tarikh

    tarikh = (time.strftime("%Y%m%d"))
    sdir = "/storage/extSdCard/texdocs/iotd/"
    failtex = sdir+"iotd-"+tarikh+".tex"
    failkeluar = open(failtex, "w")  

    w = Iotd.select().where(Iotd.date == tarikh)

    print >>failkeluar,"\documentclass[12pt,a5paper]{article}\n\
    \usepackage{palatino}\n\
    \usepackage{nopageno}\n\
    \usepackage{floatflt}\n\
    \usepackage[top=3.3cm,bottom=3.3cm, left=0.3cm,right=0.3cm]{geometry}\n\
    \usepackage{pdflscape,soul}\n\
    \usepackage{pifont}\n\
    \usepackage{graphicx}\n\
    \usepackage{xcolor}\n\
    \setlength\parindent{0pt}\n\n\
    \\begin{document}\n\n\
    \\begin{landscape}\n\
    \\Huge\n\
    \\centerline{\\textcolor{orange}{\\so{IDIOM OF THE DAY}}}\n\
    \\medskip\n\
    \\begin{center}\n"
    for i in w:
        print i.idiom, i.meaning, i.sentence+"\n"
        print >>failkeluar,"\\textbf{\\so{%s}} \n\n \\medskip" % i.idiom
        print >>failkeluar," \\textit{%s} "   %   i.meaning
        print >>failkeluar,"\\medskip \n"
        print >>failkeluar,"\\texttt{%s}\n\n"   % i.sentence
        print >>failkeluar,"\\vfill\n\n"
        print >>failkeluar,"\\textcolor{red}{\dingline{105}}\n\n\
    \\end{center}\n\n\
    \\end{landscape}\n\
    \\end{document}"

    failkeluar.close()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def searchword():
    reload(sys) 
    sys.setdefaultencoding('utf8')
    print "Cari perkataan daripada Word\n"
    kata = raw_input("Masukkan perkataan: \n")
    u = Wotd.select().where(Wotd.word.contains(kata))
    for i in u:
        print "="*len(i.word)+"\n"+str(i.word)+"\n"+"="*len(i.word)+"\n"+i.meaning+"\n"+i.sentence
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def searchidiom():
    reload(sys)
    sys.setdefaultencoding('utf8')
    print "Cari peribahasa daripada Word\n"
    kata = raw_input("Masukkan peribahasa: \n")
    u = Iotd.select().where(Iotd.idiom.contains(kata))
    for i in u:
        print "="*len(i.idiom)+"\n"+str(i.idiom)+"\n"+"="*len(i.idiom)+"\n"+i.meaning+"\n"+i.sentence
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def searchmuet():
    reload(sys) 
    sys.setdefaultencoding('utf8')
    print "Cari perkataan daripada MUET\n"
    kata = raw_input("Masukkan perkataan: \n")
    u = Muetvocab.select().where(Muetvocab.word.contains(kata))
    for i in u:
        print "="*len(i.word)+"\n"+str(i.word)+"\n"+"="*len(i.word)+"\n"+i.kata+"\n"+i.sentence
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def searchquestionsfb():
    reload(sys) 
    sys.setdefaultencoding('utf8')
    print "Search question FB\n"
    item = raw_input("Enter item: \n")
    u = Questionsfb.select().where(Questionsfb.item.contains(item))
    print "="*30
    for i in u:
        print i.item+" Answer: "+str(i.answer)
    print "="*30
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def searchquestionsfbtopicid():
    reload(sys) 
    sys.setdefaultencoding('utf8')
    print "Search question FB topic id\n"
    number = raw_input("Enter topic id number: \n")
    u = Questionsfb.select().where(Questionsfb.topicid == number)
    print "="*30
    for i in u:
        print i.item+" Answer: "+str(i.answer)
    print "="*30
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def writeboth():
    writeword()
    writeidiom()

def addquestionmaster():
    masa = (time.strftime("%Y-%m-%d %H:%M:%S"))
    print "Add Question Master"
    cat = raw_input("Enter category: \n")
    cat = cat.strip().lower()
    level = raw_input("Enter level: \n")
    level = level.strip().lower()
    source = raw_input("Enter the source: \n")
    source = source.strip().lower()
    topic = raw_input("Enter topic: \n")
    topic = topic.strip().lower()
    type = raw_input("Enter type: \n")
    type = type.strip().lower()
    instructions = raw_input("Enter instruction(s) :\n")
    instructions = instructions.strip()
    if instructions == "":
        instructions = "-"
    else:
        instructions = instructions
    suggestions = raw_input("Enter suggestions (answers etc) :\n")
    suggestions = suggestions.strip()
    if suggestions == "":
        suggestions = "-"
    else:
        suggestions = suggestions
    tarikh = raw_input("Enter the date [YYYYMMDD]:\n")
    if tarikh == "":
        tarikh = masa
    else:
        tarikh = tarikh
    print tarikh
    simpan = Questionsmaster.insert(cat=cat, level=level, source=source,\
                         time=tarikh,topic=topic, type=type, instructions=instructions, suggestions=suggestions).execute()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def addquestionfb():
    masa = (time.strftime("%Y%m%d %H:%M:%S"))
    print "Add Question FB"
    item = raw_input("Enter question: \n")
    item = item.strip()
    answer = raw_input("Enter answer: \n")
    answer = answer.strip()
    topicid = raw_input("Enter topicid (no - questionmaster): \n")
    topicid = topicid.strip()
    simpan = Questionsfb.insert(item=item, answer=answer, topicid=topicid)\
                         .execute()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def addweburl():
    masa = (time.strftime("%Y%m%d %H:%M:%S"))
    print "Add Web Content"
    content = raw_input("Enter content: \n")
    content = content.strip()
    url = raw_input("Enter URL: \n")
    if url == "":
        url = "-"
    else:
        url = url
    url = url.strip()
    tags = raw_input("Enter tag(s): \n")
    if tags == "":
        tags = "-"
    else:
        tags = tags
    tags = tags.strip()
    simpan = Webcontents.insert(content=content, url=url, tags=tags).execute()


def buildstatistics():
    statword = Wotd.select(fn.count(Wotd.word)).scalar()
    statidiom = Iotd.select(fn.count(Iotd.idiom)).scalar()
    stattip = Totd.select(fn.count(Totd.issue)).scalar()
    statmuet = Muetvocab.select(fn.count(Muetvocab.word)).scalar()
    print "Word: "+str(statword)
    print "Idiom: "+str(statidiom)
    print "MUET: "+str(statmuet)
    print "Tip: "+str(stattip)
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


def sendingwordandidioms():

    today = datetime.datetime.today()
    adaybefore = today - datetime.timedelta(days=1)
    tarikh = (time.strftime("%Y%m%d"))
    semalam = adaybefore.strftime("%Y-%m-%d")

    sdirwotd = "/storage/extSdCard/texdocs/wotd/"
    filenamewotd = "wotd-"+tarikh+".pdf.jpg" 
    fullpathfilenamewotd = sdirwotd+"wotd-"+tarikh+".pdf.jpg"    

    sdiriotd = "/storage/extSdCard/texdocs/iotd/"
    filenameiotd = "iotd-"+tarikh+".pdf.jpg" 
    fullpathfilenameiotd = sdiriotd+"iotd-"+tarikh+".pdf.jpg"    
    
    fromaddr = raw_input("Enter gmail username: \n")
    masuk = getpass.getpass("Enter password: \n")
    toaddr = "nege725saze@post.wordpress.com"
    server01 = smtplib.SMTP('smtp.gmail.com' ,587 )
    server02 = smtplib.SMTP('smtp.gmail.com' ,587 )

    msgwotd = MIMEMultipart()
    msgwotd['From' ] = fromaddr
    msgwotd['To' ] = toaddr
    msgwotd['Subject' ] = "Word Of The Day"
    bodywotd = "[category word] \n\
    [tags wotd] \n\
    [status publish] \n\
    [delay "+semalam+" 22:00:00] \n\
    [end]"
    
    msgiotd = MIMEMultipart()
    msgiotd['From' ] = fromaddr
    msgiotd['To' ] = toaddr
    msgiotd['Subject' ] = "Idiom Of The Day"
    bodyiotd = "[category idiom] \n\
    [tags iotd] \n\
    [status publish] \n\
    [delay "+semalam+" 22:05:00] \n\
    [end]"
 
    
    msgwotd.attach(MIMEText(bodywotd, 'plain' ))
    attachmentwotd = open(fullpathfilenamewotd , "rb")
    partwotd = MIMEBase('application' , 'octet-stream' )
    partwotd.set_payload((attachmentwotd).read())
    encoders.encode_base64(partwotd)
    partwotd.add_header('Content-Disposition' , "attachment; filename=%s" % filenamewotd)
    msgwotd.attach(partwotd)
    server01.starttls()
    server01.login(fromaddr , masuk)
    textwotd = msgwotd.as_string()
    server01.sendmail(fromaddr , toaddr , textwotd)
    server01.quit()

    msgiotd.attach(MIMEText(bodyiotd, 'plain' ))
    attachmentiotd = open(fullpathfilenameiotd , "rb")
    partiotd = MIMEBase('application' , 'octet-stream' )
    partiotd.set_payload((attachmentiotd).read())
    encoders.encode_base64(partiotd)
    partiotd.add_header('Content-Disposition' , "attachment; filename=%s" % filenameiotd)
    msgiotd.attach(partiotd)
    server02.starttls()
    server02.login(fromaddr , masuk)
    textiotd = msgiotd.as_string()
    server02.sendmail(fromaddr , toaddr , textiotd)
    server02.quit()
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
    with open(backupdir+'dump-english-'+harini+'.sql', 'w') as f:
        for line in con.iterdump():
            f.write('%s\n' % line)
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def menulist():
    for key, value in menu_actions.iteritems():
        print str(key)+" : "+str(value)
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
    'aw': addword,
    'ai': addidiom,
    'am': addmuet,
    'aqm': addquestionmaster,
    'aqfb': addquestionfb,
    'at': addtip,
    'aweb': addweburl,
    'bu':  peliharadata,
    'co': buildstatistics,
    'it': idiomtomorrow,
    'm': menulist,
    'se': sendingwordandidioms,
    'sqfb': searchquestionsfb,
    'sqto': searchquestionsfbtopicid,
    'sw': searchword,
    'sweb': searchweburl,
    'si': searchidiom,
    'sm': searchmuet,
    'st': searchtip,
    'wt': wordtomorrow,
    'wb': writeboth,
    'wi': writeidiom,
    'ww': writeword,
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
