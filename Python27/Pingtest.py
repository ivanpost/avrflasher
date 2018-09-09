#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys
import pyping

hostname = '192.168.31.12'

r = pyping.ping(hostname)

if r.ret_code == 0:
    print("Ping OK")
    sys.exit(0)
else:
    print("Not OK")
