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
from peewee import *

if os.path.exists('/storage/extSdCard'):
    database = SqliteDatabase('/storage/extSdCard/mydb/9510305.sqlite', **{})
else:
    database = SqliteDatabase('9510305.sqlite', **{})



class BaseModel(Model):
    class Meta:
        database = database

class Childrenmalengvocab(BaseModel):
    category = TextField(null=True)
    kata = TextField(null=True)
    level = TextField(null=True)
    note = TextField(null=True)
    word = TextField(unique=True)

    class Meta:
        db_table = 'children-mal-eng-vocab'

class Foto(BaseModel):
    aktiviti  = TextField(null=True)
    anjuran  = TextField(null=True)
    catatan  = TextField(null=True)
    masa = TextField(null=True)
    peristiwa  = TextField(null=True)
    tarikh = TextField()
    tetamu  = TextField(null=True)

    class Meta:
        db_table = 'foto'

class Hoye001(BaseModel):
    masa = DateTimeField(null=True)
    nota = CharField(null=True)

    class Meta:
        db_table = 'hoye001'

class Hutang(BaseModel):
    perkara = CharField(null=True)
    rm = TextField(null=True)  # num
    tarikh = IntegerField(null=True)

    class Meta:
        db_table = 'hutang'

class Ingat2015(BaseModel):
    id = IntegerField(null=True)
    kuadran = CharField(null=True)
    masa = DateTimeField(null=True)
    nota = CharField(null=True)
    perkara = CharField()
    status = CharField(null=True)

    class Meta:
        db_table = 'ingat2015'        
        
class Soruogos2014(BaseModel):
    perkara = TextField()
    rm = TextField()
    tarikh = TextField()

    class Meta:
        db_table = 'soruogos2014'


today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)
esok = tomorrow.strftime("%Y%m%d")
 
tahunini = datetime.datetime.today().year
bulanini = today.strftime("%Y%m")

# Main definition - constants
menu_actions  = {}  

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    
    print ":: Hoye ::\n"
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


#-----------------------------------------------------------------------    

def masukhoye():
    tarikh = raw_input("Masukkan tarikh: \n")
    if tarikh == "":
        tarikh = today.strftime("%Y-%m-%d %H:%M:%S")
    else:
        tarikh = tarikh
    print tarikh

    nota = raw_input("Masukkan nota: \n")
    simpan = Hoye001.insert(masa=tarikh,nota=nota).execute()
    print "\n"+tarikh+"\n"+nota+"\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def carihoye():
    reload(sys)
    sys.setdefaultencoding('utf8')
    print "Cari dalam hoye001\n"
    kata = raw_input("Masukkan perkataan: \n")
    u = Hoye001.select().where(Hoye001.nota.contains(kata))
    for i in u:
        print "\n"+str(i.masa)+"\n\n"+str(i.nota)+"\n\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def masuksoru():
    tarikh = raw_input("Masukkan tarikh: \n")
    if tarikh == "":
        tarikh = today.strftime("%Y%m%d")
    else:
        tarikh = tarikh
    print tarikh

    perkara = raw_input("Masukkan perkara: \n")
    perkara = perkara.strip()

    rm = raw_input("Masukkan RM: \n")
    rm = rm.strip()
    simpan = Soruogos2014.insert(tarikh=tarikh,perkara=perkara, rm=rm).execute()
    print "\n"+tarikh+"::"+perkara+" : "+rm
    belanja =\
    Soruogos2014.select(fn.Sum(Soruogos2014.rm)).where(Soruogos2014.tarikh ==\
                                                      tarikh).scalar()
    senarai =\
    Soruogos2014.select().where(Soruogos2014.tarikh == tarikh)
    print "="*40
    for i in senarai:
        print i.perkara, i.rm
    print "="*40
    print "Jumlah hari ini : RM "+str(belanja)
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def semaktarikh():
    tarikh = raw_input("Masukkan tarikh: \n")
    if tarikh == "":
        tarikh = today.strftime("%Y%m%d")
    else:
        tarikh = tarikh
    print tarikh
    senarai =\
    Soruogos2014.select().where(Soruogos2014.tarikh == tarikh)
    print "="*40
    for i in senarai:
        print i.perkara, i.rm
    print "="*40
    belanja =\
    Soruogos2014.select(fn.Sum(Soruogos2014.rm)).where(Soruogos2014.tarikh ==\
                                                      tarikh).scalar()
    print "Jumlah hari ini : RM "+str(belanja)
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

    perkara = raw_input("Masukkan perkara: \n")
    perkara = perkara.strip()

def semakperkara():
    perkara = raw_input("Masukkan perkara: \n")
    u =\
    Soruogos2014.select().where(Soruogos2014.perkara.contains(perkara)).order_by(Soruogos2014.tarikh)
    print "="*20
    for i in u:
        print str(i.tarikh)+" :"+" : "+str(i.perkara)+" : "+str(i.rm)
    print "="*20
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def masukingat():
    tarikh = raw_input("Masukkan tarikh: \n")
    if tarikh == "":
        tarikh = today.strftime("%Y%m%d")
    else:
        tarikh = tarikh
    print tarikh

    perkara = raw_input("Masukkan perkara: \n")
    
    nota = raw_input("Masukkan nota: \n") or "-"
    kuadran = raw_input("Masukkan kuadran: \n") or "2"
    simpan =  Ingat2015.insert(masa=tarikh,perkara=perkara, nota=nota, status = "belum", kuadran = kuadran).execute()
    print "\n"+tarikh+"\n"+perkara+"\n"+kuadran+"\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return        

def cariingat():
    reload(sys)
    sys.setdefaultencoding('utf8')
    print "Cari dalam Ingat\n"
    kata = raw_input("Masukkan perkataan: \n")
    u = Ingat2015.select().where(Ingat2015.perkara.contains(kata))
    for i in u:
        print str(i.masa)+" : "+str(i.perkara)+"("+i.kuadran+")\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def cariingatk2():
    u = Ingat2015.select().where(Ingat2015.kuadran == 2).order_by(-Ingat2015.masa)
    print "="*30
    for i in u:
        print str(i.masa)+" : "+str(i.perkara)+"("+i.kuadran+")\n"
    print "="*30
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
def buatsiap(): 
    u = Ingat2015.select().where(Ingat2015.status ==\
                                  'belum')&(Ingat2015.status=="2").order_by(Ingat2015.masa)
    for i in u:
        print "["+str(i.id)+"] "+ str(i.masa)+":: "+i.perkara+" :: ("+str(i.kuadran)+")"

    selectingatid = raw_input("Masukkan id ingat: \n ")
    query = Ingat2015.update(\
                status="selesai").\
               where(Ingat2015.id == selectingatid)
    query.execute()
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def masukhutang():
    tarikh = raw_input("Masukkan tarikh: \n")
    if tarikh == "":
        tarikh = today.strftime("%Y%m%d")
    else:
        tarikh = tarikh
    print tarikh

    perkara = raw_input("Masukkan perkara: \n")
    
    rm = raw_input("Masukkan RM: \n")
    simpan = Hutang.insert(tarikh=int(tarikh),perkara=perkara, rm=rm).execute()
    print "\n"+tarikh+"\n"+perkara+"\n"+rm+"\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def carihutang():
    print "Cari dalam Hutang\n"
    kata = raw_input("Masukkan perkataan: \n")
    u = Hutang.select().where(Hutang.perkara.contains(kata))
    for i in u:
        print str(i.tarikh)+" : "+str(i.perkara)+"("+i.rm+")\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
    
def carihutangtarikh():
    print "Cari tarikh hutang\n"
    hb1 = raw_input("Masukkan tarikh mula [YYYYMMDD]: \n")
    hb2 = raw_input("Masukkan tarikh akhir [YYYYMMDD]: \n")
    u = Hutang.select().where(Hutang.tarikh.between(hb1, hb2))
    for i in u:
        print str(i.tarikh)+" : "+str(i.perkara)+"("+i.rm+")\n"
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
    'bs': buatsiap,
    'ch': carihoye,
    'ci': cariingat,
    'chu': carihutang,
    'chuta': carihutangtarikh,
    'ckd': cariingatk2,
    'cv': calendarview,
    'ho': masukhoye,
    'hu': masukhutang,
    'ms': masuksoru,
    'mi': masukingat,
    'sp': semakperkara,
    'st': semaktarikh,
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
