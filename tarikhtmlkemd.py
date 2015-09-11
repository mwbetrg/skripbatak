#!/usr/bin/python
#Created : Fri 14 Aug 2015 09:09:52 AM UTC
#Last Modified : Fri 14 Aug 2015 09:35:07 AM UTC

import os
import sys
import datetime
from time import strftime
from html2text import cli

import site

harini = datetime.datetime.today()
tarikh = harini.strftime("%Y%m%d")

laman = raw_input("Masukkan URL: \n")
namafail = raw_input("Masukkan nama fail: \n")

sdir = "/tmp/"

html2text.py laman # > sdir+str(tarikh)+namafail+".md"
