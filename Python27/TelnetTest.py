#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
import telnetlib
import sys


try:
    tn = telnetlib.Telnet("192.168.31.36", 23, 3)
except:
    print 'Error telnet'
    sys.exit(0)
tn.close()
print 'Telnet OK'
tn.close()
