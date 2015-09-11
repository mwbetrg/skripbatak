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
from glob import glob


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

def deletewhatsappdatabases():
    selecteddir = '/storage/emulated/0/WhatsApp/Databases/'
    for f in os.listdir(selecteddir):
        print f
        if re.search('msgstore-20(.*)crypt8'):
            os.remove(os.path.join(selecteddir, f))
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def deletewordfiles():
    selecteddir = '/storage/extSdCard/texdocs/wotd/'
    for f in os.listdir(selecteddir):
        print f
        if re.search('wotd-20(.*).jpg'):
            os.remove(os.path.join(selecteddir, f))
        if re.search('wotd-20(.*).aux'):
            os.remove(os.path.join(selecteddir, f))
        if re.search('wotd-20(.*).log'):
            os.remove(os.path.join(selecteddir, f))
        if re.search('wotd-20(.*).pdf'):
            os.remove(os.path.join(selecteddir, f))
        if re.search('wotd-20(.*).pdf.jpg'):
            os.remove(os.path.join(selecteddir, f))
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def deleteidiomfiles():
    selecteddir = '/storage/extSdCard/texdocs/iotd/'
    for f in os.listdir(selecteddir):
        print f
        if re.search('iotd-20(.*).jpg'):
            os.remove(os.path.join(selecteddir, f))
        if re.search('iotd-20(.*).aux'):
            os.remove(os.path.join(selecteddir, f))
        if re.search('iotd-20(.*).log'):
            os.remove(os.path.join(selecteddir, f))
        if re.search('iotd-20(.*).pdf'):
            os.remove(os.path.join(selecteddir, f))
        if re.search('iotd-20(.*).pdf.jpg'):
            os.remove(os.path.join(selecteddir, f))
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def deleteenglishfiles():
    deletewordfiles()
    deleteidiomfiles()

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
    'cv': calendarview,
    'dwd': deletewhatsappdatabases,
    'def': deleteenglishfiles,
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
