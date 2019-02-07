#!/usr/bin/python
# coding=utf8
"""
# Author: meetbill
# Created Time : 2017-05-16 10:29:04

# File Name: monit_cli.py
# Description:
# version:1.0.3

"""
import urllib2
import monit.xmltodict
import json
import logging


class Monit(object):
    """Monit
    """
    def __init__(self, host='localhost', port=2812,
                 username=None, password='', https=False):
        """
        Args:
            host:hostname or ip
            port:monit port
            username:monit user
            password:monit password
            https:https or not
        """
        self.baseurl = (
            https and 'https://%s:%i' or 'http://%s:%i') % (host,
                                                            port)
        authinfo = urllib2.HTTPBasicAuthHandler()
        authinfo.add_password('monit', self.baseurl, username, password)
        self.opener = urllib2.build_opener(authinfo)

    def test(self):
        """test

        """
        # install_opener
        urllib2.install_opener(self.opener)
        if self._monit_status(self.baseurl) is not None:
            print "[test]:OK"
        else:
            print "[test]:ERR"

    def _monit_status(self, url):
        response = None
        try:
            response = urllib2.urlopen(url, timeout=5)
        except Exception as e:
            if hasattr(e, 'code'):
                if e.code == 401:
                    logging.error("[url]:%s [error]:auth failure" % url)
                else:
                    logging.error(
                        "[url]:%s [error]:another error [e.code]:%s" %
                        (url, e.code))
            logging.error("[url]:%s [error]:%s [e]:%s" % (url, Exception, e))
        return response

    def status(self):
        """Output  Monit deamon and services status.
        Return:
            monit status(dict)
        """
        result = None
        url = self.baseurl + '/_status?format=xml'
        urllib2.install_opener(self.opener)
        response = self._monit_status(url)
        if response is None:
            return result
        status_xml = response.read().split('?>')[1]

        result = monit.xmltodict.parse(status_xml)
        return result


if __name__ == "__main__":
    mon = Monit(
        host='127.0.0.1',
        port=2812,
        username='admin',
        password='monit')
    mon.test()
    print json.dumps(mon.status(), indent=4)
