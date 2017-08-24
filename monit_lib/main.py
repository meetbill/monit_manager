#!/usr/bin/python
#coding=utf8
"""
# Author: meetbill
# Created Time : 2017-05-16 10:29:04

# File Name: main.py
# Description:
# version:1.0.2

"""
import urllib2
import my_lib.xmltodict
import sys
import json

class Monit():
    def __init__(self, host='localhost', port=2812, username=None, password='', https=False):
        self.baseurl = (https and 'https://%s:%i' or 'http://%s:%i') % (host, port)
        if username:
            authinfo = urllib2.HTTPBasicAuthHandler()
            authinfo.add_password('monit',self.baseurl,username,password)
            self.opener=urllib2.build_opener(authinfo)
        try:
            # install_opener
            urllib2.install_opener(self.opener)
            # check auth
            urllib2.urlopen(self.baseurl,timeout=5)
        except Exception,e:
            if hasattr(e, 'code'):  
                if e.code == 401:
                    print "[ERROR] auth failure"
                    sys.exit()
                else:
                    print 'We got another error'  
                    print e.code  
            print Exception,":",e
            print("the monit is not running")
            sys.exit()
    def status(self):
        """
        Update Monit deamon and services status.
        """
        url = self.baseurl + '/_status?format=xml'
        urllib2.install_opener(self.opener)
        response = urllib2.urlopen(url,timeout=5)
        status_xml = response.read().split('?>')[1]
        # print status_xml

        root_info = my_lib.xmltodict.parse(status_xml)
        #root_info = my_lib.xmldict.xml_to_dict(str(response.text))
        # print root_info
        print json.dumps(root_info,indent=4)

if __name__ == "__main__":
    from pydoc import render_doc
    import argparse
    mon = Monit(username='admin', password='monit')
    parser=argparse.ArgumentParser(usage='\033[43;37mpython %(prog)s function param [options]\033[0m')
    options, unknown_args = parser.parse_known_args()
    options = vars(options)
    if not unknown_args:
        print(parser.print_help())
        print(render_doc(Monit))
        exit()
    func = unknown_args.pop(0)
    
    try:
        cmd = getattr(mon, func)
    except:
        print('No such function: %s' % func)
        print(render_doc(Monit))
        exit()

    try:
        kwargs = {}
        func_args = []
        for arg in unknown_args:
            if '=' in arg:
                key, value = arg.split('=', 1)
                kwargs[key] = value
            else:
                func_args.append(arg)
        func_args = tuple(func_args)
        function_result = cmd(*func_args, **kwargs)
    except TypeError:
        print(render_doc(cmd))
        exit()
