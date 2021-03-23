import sys,os,re,socket,binascii,time,json,random,threading,Queue,pprint,urlparse,smtplib,telnetlib,os.path,hashlib,string,urllib2,glob,sqlite3,urllib,argparse,marshal,base64,requests
from colorama import *
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
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

def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """ 
  ______                      _       _     ____            _      __      __  __   _  _   
 |___  /                     | |     (_)   |  _ \          | |     \ \    / / /_ | | || |  
    / /    ___    _ __ ___   | |__    _    | |_) |   ___   | |_     \ \  / /   | | | || |_ 
   / /    / _ \  | '_ ` _ \  | '_ \  | |   |  _ <   / _ \  | __|     \ \/ /    | | |__   _|
  / /__  | (_) | | | | | | | | |_) | | |   | |_) | | (_) | | |_       \  /     | |    | |  
 /_____|  \___/  |_| |_| |_| |_.__/  |_|   |____/   \___/   \__|       \/      |_|    |_|  
    
	ICQ: @viper1337official
                                                                                                                                                                                                                                                                                      
 1) Zombi Bot V14 Scanner Pro         11) Viper 1337 private Scanner V2.0
 2) Advance Mass Url Collector        12) Mass Shell Checker   
 3) Email Filter                      13) Mass Shell Mail Function Checker
 4) Hash Cracker V1.0                 14) Mass Shell Upload Anything Bot
 5) Grabber Ip From Domains List      15) Mass zone-h Grabber
 6) Viper 1337 SMTP Cracker v2        16) Viper1337 Private Tools   
 7) cPanel Cracker V3.0               17) CMS Filter
 8) Mass cPanel Checker               18) 0day Private Bot
 9) Mass cPanel Reset By Shell        19) Remove Duplicated Lines
10) Mass cPanel Upload Anything       20) Check For Latest Update
             	  		  
			                  """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)


logo()


choice=raw_input('Choose Number => ')
if choice=='1':
  print("""\n\033[91m Go to Files/Tool1 and put ur list of sites there
	result will be in folder reasult with name 

 y = yes 
 n = no\033[0m""")
  t=raw_input('~>')
  if t=='y':
   if system() == 'Linux':
    os.system("cd Files/Tool1 && chmod +x v14.py && python v14.py")
   if system() == 'Windows':
    os.system('cd Files/Tool1 && v14.py && list.txt')
   else:
    print('unknown error :| ')
  elif t=='n':
   main()
  else :
   print('unknown error :| ')
elif choice=='2':
  print("""\n\033[91m  Put Your Dork List. Result Will Be Get Files/Tool2 with name .
	
 y = yes 
 n = no\033[0m""")
  t=raw_input('~>')
  if t=='y':
   if system() == 'Linux':
    os.system("cd Files/Tool2 && chmod +x dorker.py && python dorker.py")
   if system() == 'Windows':
    os.system('cd Files/Tool2 && dorker.py')
   else:
    print('unknown error :| ')
  elif t=='n':
   main()
  else :
   print('unknown error :| ')
elif choice=='3':
  print("""\n\033[91m Put Ur Email List. Then Result Will Be Saved In Files\Tool3\Filtred With The Name
 y = yes 
 n = no\033[0m""")
  t=raw_input('~>')
  if t=='y':
   if system() == 'Linux':
    os.system("cd Files/Tool3 && chmod +x filter.py && python filter.py")
   if system() == 'Windows':
    os.system('cd Files/Tool3 && filter.py')
   else:
    print('unknown error :| ')
  elif t=='n':
   main()
  else :
   print('unknown error :| ')
elif choice=='4':
  print("""\n\033[91m 
 y = yes 
 n = no\033[0m""")
  t=raw_input('~>')
  if t=='y':
   if system() == 'Linux':
    os.system("cd Files/Tool4 && chmod +x hashti.py && python hashti.py")
   if system() == 'Windows':
    os.system('cd Files/Tool4 && hashti.py')
   else:
    print('unknown error :| ')
  elif t=='n':
   main()
  else :
   print('unknown error :| ')
elif choice=='5':
  print("""\n\033[91m Go to Files/Tool5  Just Add Ur Domain List There
Note Domain Without Http://
Exemple : google.com  
 y = yes 
 n = no\033[0m""")
  t=raw_input('~>')
  if t=='y':
   if system() == 'Linux':
    os.system("cd Files/Tool5 && chmod +x ip.py && python ip.py")
   if system() == 'Windows':
    os.system('cd Files/Tool5 && ip.py')
   else:
    print('unknown error :| ')
  elif t=='n':
   main()
  else :
   print('unknown error :| ')
elif choice=='6':
  print("""\n\033[91m Go to Files/Tool6 Put Your Email List .
 y = yes 
 n = no\033[0m""")
  t=raw_input('~>')
  if t=='y':
   if system() == 'Linux':
    os.system("cd Files/Tool6 && chmod +x smtp.py && python smtp.py")
   if system() == 'Windows':
    os.system('cd Files/Tool6 && smtp.py')
   else:
    print('unknown error :| ')
  elif t=='n':
   main()
  else :
   print('unknown error :| ')
elif choice=='7':
  print("""\n\033[91m Go to Files/Tool7
Put Your URLS list of Sites in domain.txt
 y = yes 
 n = no\033[0m""")
  t=raw_input('~>')
  if t=='y':
   if system() == 'Linux':
    os.system("cd Files/Tool7 && chmod +x python bruter.py 50 domain.txt password.txt && python bruter.py 50 domain.txt password.txt")
   if system() == 'Windows':
    os.system('cd Files/Tool7 && python bruter.py 50 domain.txt password.txt')
   else:
    print('unknown error :| ')
  elif t=='n':
   main()
  else :
   print('unknown error :| ')
elif choice=='8':
  print("""\n\033[91m 
 y = yes 
 n = no\033[0m""")
  t=raw_input('~>')
  if t=='y':
   if system() == 'Linux':
    os.system("cd Files/Tool8 && chmod +x masscp.py && python masscp.py")
   if system() == 'Windows':
    os.system('cd Files/Tool8 && masscp.py')
   else:
    print('unknown error :| ')
  elif t=='n':
   main()
  else :
   print('unknown error :| ')
elif choice=='9':
  print("""\n\033[91m
 y = yes 
 n = no\033[0m""")
  t=raw_input('~>')
  if t=='y':
   if system() == 'Linux':
    os.system("cd Files/Tool9 && chmod +x cpreset.py && python cpreset.py")
   if system() == 'Windows':
    os.system('cd Files/Tool9 && cpreset.py')
   else:
    print('unknown error :| ')
  elif t=='n':
   main()
  else :
   print('unknown error :| ')
elif choice == '10':
    print("""\n\033[91m 
 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool10 && chmod +x masscp.py && python masscp.py ")
        if system() == 'Windows':
            os.system('cd Files/Tool10 && masscp.py')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')
elif choice == '11':
    print("""\n\033[91m Go to Files/Tool11 Put Your URLS list of Sites in list.txt . Result Will Be Save On Files/Tool11/Result
Then  Run it
 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool11 && chmod +x private.py && python private.py ")
        if system() == 'Windows':
            os.system('cd Files/Tool11 && private.py')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')
elif choice == '12':
    print("""\n\033[91m Go to Files/Tool12 Put Your Shell on list.txt
 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool12 && chmod +x shellchecker.py && python shellchecker.py ")
        if system() == 'Windows':
            os.system('cd Files/Tool12 && shellchecker.py')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')
elif choice == '13':
    print("""\n\033[91m Go to Files/Tool13
	 Put Your WSO Shell List There
Then  Run it
 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool13 && chmod +x mscs.py && python mscs.py ")
        if system() == 'Windows':
            os.system('cd Files/Tool13 && mscs.py')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')
elif choice == '14':
    print("""\n\033[91m Go to Files/Tool14 
	Put Your WSO Shell List There
 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool14 && chmod +x msua.py && python msua.py ")
        if system() == 'Windows':
            os.system('cd Files/Tool14 && msua.py')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')
   
elif choice == '15':
    print("""\n\033[91m 
 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool15 && chmod +x zone.py && python zone.py")
        if system() == 'Windows':
            os.system('cd Files/Tool15 && zone.py')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')   
elif choice == '16':
    print("""\n\033[91m 
 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool16 && chmod +x private.py && python private.py")
        if system() == 'Windows':
            os.system('cd Files/Tool16 && private.py')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')   
elif choice == '17':
    print("""\n\033[91m Go to Files/Tool17 Put Your URL List 
	
 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool17 && chmod +x cms.py && python cms.py")
        if system() == 'Windows':
            os.system('cd Files/Tool17 && cms.py')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')   
      
elif choice == '18':
    print("""\n\033[91m Go to Files/Tool18 
	Put Url Lst

 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool18 && chmod +x 0day.py && python 0day.py")
        if system() == 'Windows':
            os.system('cd Files/Tool18 && 0day.py')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')     
elif choice == '19':
    print("""\n\033[91m 

 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool19 && chmod +x dup.py && python dup.py")
        if system() == 'Windows':
            os.system('cd Files/Tool19 && dup.py')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')     
elif choice == '20':
    print("""\n\033[91m 

 y = yes 
 n = no\033[0m""")
    t = raw_input('~>')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Files/Tool20 && chmod +x Update.txt && text Update.txt")
        if system() == 'Windows':
            os.system('cd Files/Tool20 && Update.txt')
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')    
   

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
