#!/usr/bin/python
#coding=utf8
"""
# Author: meetbill
# Created Time : 2017-05-16 10:29:04

# File Name: main.py
# Description:
# version:0.1

"""
import requests
import my_lib.xmldict
import sys

class Monit(dict):
    def __init__(self, host='localhost', port=2812, username=None, password='', https=False):
        self.baseurl = (https and 'https://%s:%i' or 'http://%s:%i') % (host, port)
        if username:
            self.auth = requests.auth.HTTPBasicAuth(username, password)
        try:
            r = requests.get(self.baseurl,auth=self.auth)
            if not (r.status_code == 200):
                print("the password is not right")
                sys.exit()
        except Exception,e:
            #print Exception,":",e
            print("the monit is not running")
            sys.exit()
    def update(self):
        """
        Update Monit deamon and services status.
        """
        url = self.baseurl + '/_status?format=xml'
        response = requests.get(url, auth=self.auth)
        root_info = my_lib.xmldict.xml_to_dict(str(response.text))
        print root_info

if __name__ == "__main__":
    mon = Monit(username='admin', password='monit')
    mon.update()
