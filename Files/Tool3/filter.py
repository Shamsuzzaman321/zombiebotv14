#!/usr/bin/python
 # -*-coding:Latin-1 -*
import sys,urllib2
from colorama import *

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore								
from colorama import Style								
from termcolor import colored
import requests, sys, re, os, time, random
from colorama import Fore, Back, Style
init()

la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'
r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

  ______                      _       _     ____            _      __      __  __   _  _   
 |___  /                     | |     (_)   |  _ \          | |     \ \    / / /_ | | || |  
    / /    ___    _ __ ___   | |__    _    | |_) |   ___   | |_     \ \  / /   | | | || |_ 
   / /    / _ \  | '_ ` _ \  | '_ \  | |   |  _ <   / _ \  | __|     \ \/ /    | | |__   _|
  / /__  | (_) | | | | | | | | |_) | | |   | |_) | | (_) | | |_       \  /     | |    | |  
 /_____|  \___/  |_| |_| |_| |_.__/  |_|   |____/   \___/   \__|       \/      |_|    |_|  
                                                                                                                                   ICQ: @viper1337official                                   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()
def fitromailon(x, y):
    if x!=0 :
      print "   %s[%s+%s]%s %s : %s"%(la7mar,lazra9,la7mar,la5dhar,y,x)

def filterspy():


   nb=0
   notmail=0
   Yahoo=0
   Mailru=0
   inboxru=0
   bkru=0
   hotmail=0
   live=0
   outlook=0
   seznamcz=0
   gmail=0
   orangefr=0
   yandex=0
   gmx=0
   TunisienShitt=0
   aol=0
   freefr=0
   rambler=0
   citromailhu=0
   cncom=0
   Freenetde=0
   freemailhu=0
   abv=0
   tonlinede=0
   op=0
   onet=0
   vp=0
   other=0
   burn =str(raw_input("Email List Name :"))
   if not os.path.isdir('Filtred'):
    os.mkdir('Filtred')
   with open(burn, 'r') as earth:
      file = earth.read().splitlines()
   for fade in file:
    fade=fade.lower()
    nb=nb+1
    try:
     if '@' not in str(fade):
        notmail=notmail+1
     elif '@yahoo.' in str(fade):
        Yahoo=Yahoo+1
        zzz=open('Filtred/yahoo.txt','a')
        zzz.write(fade+'\n')
     elif '@mail.ru' in str(fade):
        Mailru=Mailru+1
     elif  '@inbox.ru' in str(fade):
        inboxru=inboxru+1
        zzz=open('Filtred/inbox.ru.txt','a')
        zzz.write(fade+'\n')
     elif  '@bk.ru' in str(fade):
        bkru=bkru+1
        zzz=open('Filtred/bk.ru.txt','a')
        zzz.write(fade+'\n')
     elif  '@hotmail' in str(fade):
        hotmail=hotmail+1
        zzz=open('Filtred/hotmail.txt','a')
        zzz.write(fade+'\n')
     elif  '@live' in str(fade):
        live=live+1
        zzz=open('Filtred/live.txt','a')
        zzz.write(fade+'\n')
     elif  '@outlook' in str(fade):
        outlook=outlook+1
        zzz=open('Filtred/outlook.txt','a')
        zzz.write(fade+'\n')
     elif '@seznam.cz' in str(fade):
        seznamcz=seznamcz+1
        zzz=open('Filtred/seznam.cz.txt','a')
        zzz.write(fade+'\n')
     elif '@gmail.com' in str(fade):
        gmail=gmail+1
        zzz=open('Filtred/gmail.com.txt','a')
        zzz.write(fade+'\n')
     elif '@orange.' in str(fade):
        orangefr=orangefr+1
        zzz=open('Filtred/orange.fr.txt','a')
        zzz.write(fade+'\n')
     elif '@yandex.' in str(fade):
        yandex=yandex+1
        zzz=open('Filtred/yandex.txt','a')
        zzz.write(fade+'\n')
     elif '@gmx.' in str(fade):
        gmx=gmx+1
        zzz=open('Filtred/gmx.txt','a')
        zzz.write(fade+'\n')
     elif '.tn' in str(fade):
        TunisienShitt=TunisienShitt+1
        zzz=open('Filtred/tona.txt','a')
        zzz.write(fade+'\n')
     elif '@aol.' in str(fade):
        aol=aol+1
        zzz=open('Filtred/aol.txt','a')
        zzz.write(fade+'\n')
     elif '@free.fr' in str(fade):
        freefr=freefr+1
        zzz=open('Filtred/free.fr.txt','a')
        zzz.write(fade+'\n')
     elif '@rambler.' in str(fade):
        rambler=rambler+1
        zzz=open('Filtred/rambler.txt','a')
        zzz.write(fade+'\n')
     elif '@citromail.hu' in str(fade):
        citromailhu=citromailhu+1
        zzz=open('Filtred/citromail.txt','a')
        zzz.write(fade+'\n')
     elif '@21cn.com' in str(fade):
        cncom=cncom+1
        zzz=open('Filtred/21cn.com.txt','a')
        zzz.write(fade+'\n')
     elif '@freenet.de' in str(fade):
        Freenetde=Freenetde+1
        zzz=open('Filtred/freenet.de.txt','a')
        zzz.write(fade+'\n')
     elif '@freemail.hu' in str(fade):
        freemailhu=freemailhu+1
        zzz=open('Filtred/freemail.hu.txt','a')
        zzz.write(fade+'\n')
     elif '@abv.bg' in str(fade):
        abv=abv+1
        zzz=open('Filtred/abv.bg.txt','a')
        zzz.write(fade+'\n')
     elif '@t-online.de' in str(fade):
        tonlinede=tonlinede+1
        zzz=open('Filtred/t.online.txt','a')
        zzz.write(fade+'\n')
     elif '@op.' in str(fade):
        op=op+1
        zzz=open('Filtred/op.txt','a')
        zzz.write(fade+'\n')
     elif '@onet.' in str(fade):
        onet=onet+1
        zzz=open('Filtred/onet.txt','a')
        zzz.write(fade+'\n')
     elif '@vp' in str(fade):
        vp=vp+1
        zzz=open('Filtred/vp.txt','a')
        zzz.write(fade+'\n')
     else:
        other=other+1
        zzz=open('Filtred/other.txt','a')
        zzz.write(fade+'\n')
    except:
            pass
   nouwa=Yahoo+Mailru+inboxru+bkru+hotmail+live+outlook+seznamcz+gmail+orangefr+yandex+gmx+TunisienShitt+aol+freefr+rambler+citromailhu+cncom+Freenetde+freemailhu+abv+tonlinede+op+onet+vp+other
   print"%s   [%s+%s] %sTotal Emails : %s"%(la7mar,lazra9,la7mar,la5dhar,nouwa)
   fitromailon(Yahoo, 'Yahoo')
   fitromailon(Mailru, 'Mail.ru')
   fitromailon(inboxru, 'Inbox.ru')
   fitromailon(bkru, 'bk.ru')
   fitromailon(hotmail, 'Hotmail')
   fitromailon(live, 'Live')
   fitromailon(outlook, 'Outlook')
   fitromailon(seznamcz, 'seznam.cz')
   fitromailon(gmail, 'Gmail')
   fitromailon(orangefr, 'Orange.fr')
   fitromailon(yandex, 'Yandex')
   fitromailon(gmx, 'Gmx')
   fitromailon(TunisienShitt, 'Tunisien Shits')
   fitromailon(aol, 'Aol')
   fitromailon(freefr, 'Free.fr')
   fitromailon(citromailhu,'citromailhu')
   fitromailon(rambler, 'Rambler')
   fitromailon(cncom, '21cn.com')
   fitromailon(Freenetde, 'Freenetde')
   fitromailon(freemailhu, 'Freemail.hu')
   fitromailon(abv, 'Abv.bg')
   fitromailon(tonlinede, 'T-online.de')
   fitromailon(op, 'op')
   fitromailon(onet, 'Onet')
   fitromailon(vp, 'Vp')
   fitromailon(other, 'Speciel Domains')
   fitromailon(notmail, 'Not E-Mail')
filterspy()
