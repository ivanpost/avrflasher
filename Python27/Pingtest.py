#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
import telnetlib
import sys

hostname = '192.168.31.12'

response = os.system("ping -c 10 192.168.31.12" )
if response == 0:
    print hostname, 'Ping OK'
else:
    print hostname, 'AQUARIUS not response!' 
    print response
    

try:
    tn = telnetlib.Telnet("192.168.31.36", 23, 3)
except:
    print 'Error telnet'
    sys.exit(0)

print 'Telnet OK' 
tn.close()
