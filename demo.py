#!/usr/bin/python
# coding=utf8
"""
# Author: meetbill
# Created Time : 2019-01-25 00:58:14

# File Name: demo.py
# Description:

"""

from monit import Monit
import json


def test_monit():
    """test monit"""
    mon = Monit(
        host='127.0.0.1',
        port=2812,
        username='admin',
        password='monit')
    mon.test()
    print json.dumps(mon.status(), indent=4)


if __name__ == "__main__":
    test_monit()
