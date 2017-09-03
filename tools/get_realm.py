#!/usr/bin/python
#coding=utf8
"""
# Author: meetbill
# Created Time : 2017-08-23 23:54:54

# File Name: get_realm.py
# Description:

"""
import urllib2  
  
theurl = 'http://127.0.0.1:2812/ping'  
req = urllib2.Request(theurl)  
try:  
    print 'urlopen begin'  
    handle = urllib2.urlopen(req)  
    print 'urlopen finish'  
except IOError, e:  
    if hasattr(e, 'code'):  
        if e.code != 401:  
            print 'We got another error'  
            print e.code  
        else:  
            print 'yes'  
            print e.headers  
            print e.headers['www-authenticate']  
    else:  
        print r'the string "code" is not in e'  
        print e  
else:  
    print 'this url can be accessed'
