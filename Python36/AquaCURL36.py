#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pycurl
import io
import time
import os.path
import telnetlib
import sys

hostname = str(input("Input Hostnname: "))

if hostname == '':
    hostname = '192.168.31.12' # Переменная ip адрес
    print('Hostname is not null, set default: ' + hostname)

hexfname = 'Aqua73.hex'  # Пременная имя файла

try:
    tn = telnetlib.Telnet(hostname, 23, 3)
except:
    print('Error connect to ' + hostname)
    sys.exit(0)
tn.close()
print('Connect to ' + hostname +' OK')
tn.close()
time.sleep(3)

url = 'http://' + hostname + '/pgm/sync'

# POST запрос - сброс uC AQUARIUS
print('Resetting Aquarius\n')
b1 = io.BytesIO()
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.TIMEOUT, 10)
c.setopt(pycurl.WRITEFUNCTION, b1.write)
c.setopt(pycurl.POSTFIELDS, 's')
c.perform()

time.sleep(3)

# GET запрос туда же - чтение результата
c.setopt(pycurl.POST, 0)
c.perform()

# Вывод результата
response_data = b1.getvalue()
c.close()
b1.close()
print(response_data)

url = 'http://' + hostname + '/pgm/upload'

# POST запрос - загрузка файла
print('\nUpload flash file in Aquarius\n')
b2 = io.BytesIO()
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.WRITEFUNCTION, b2.write)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.TIMEOUT, 10)
filesize = os.path.getsize(hexfname)
c.setopt(pycurl.POSTFIELDSIZE, filesize)
fin = open(hexfname, 'rb')
c.setopt(pycurl.READFUNCTION, fin.read)
c.perform()

# Вывод результата
response_data = b2.getvalue()
b2.close()
c.close()
print(response_data)
