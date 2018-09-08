#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pycurl
import StringIO
import time
import os.path

hostname = '192.168.31.12' # Переменная ip адрес
hexfname = 'Blink1.hex'  # Пременная имя файла 

url = 'http://' + hostname + '/pgm/sync'

# POST запрос - сброс uC AQUARIUS
print 'Resetting Aquarius\n'
b = StringIO.StringIO()
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.TIMEOUT, 10)
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.setopt(pycurl.POSTFIELDS, 's')
c.perform()

time.sleep(3)

# GET запрос туда же - чтение результата
c.setopt(pycurl.POST, 0)
c.perform()

# Вывод результата
response_data = b.getvalue()
b.truncate(0)
c.close()
print response_data

url = 'http://' + hostname + '/pgm/upload'

# POST запрос - загрузка файла
print '\nUpload flash file in Aquarius\n'
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.TIMEOUT, 10)
filesize = os.path.getsize(hexfname)
c.setopt(pycurl.POSTFIELDSIZE, filesize)
fin = open(hexfname, 'rb')
c.setopt(pycurl.READFUNCTION, fin.read)
c.perform()

# Вывод результата
response_data = b.getvalue()
b.close()
c.close()
print response_data
