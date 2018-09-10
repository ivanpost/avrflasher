#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
import sys
import pyping
hostname = str(raw_input("Input Hostnname: "))

if hostname == '':
    hostname = "192.168.31.12" # Переменная ip адрес
    print 'Hostname is not null, set default: ' + hostname
else:
    print 'Start Ping'
    
r = pyping.ping(hostname)

if r.ret_code == 0:
    print "Ping OK"
    sys.exit(0)
else:
    print "Not OK"
