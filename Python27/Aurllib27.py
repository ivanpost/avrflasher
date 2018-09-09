#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
import pycurl
import StringIO
import os.path
import pyping
import sys

hostname = '192.168.31.12' # Переменная ip адрес
hexfname = 'Blink2.hex'  # Пременная имя файла

r = pyping.ping(hostname)

if r.ret_code == 0:
    print "Ping " + hostname +" OK"
    time.sleep(1)
else:
    print "Sorry uC not response"
    sys.exit(0)

# hexfile = urllib2.urlopen("https://hi-garden.ru/images/Flash/" + hexfname)
# output = open(hexfname,'wb')
# output.write(hexfile.read())
# output.close()

url = 'http://' + hostname + '/pgm/sync'

# Данные, которые хотим отправить
query_args = { 'm':'10', 's':'', 'X':'' }

# Производим urlencodes для словаря
data = urllib.urlencode(query_args)

# Отправляем HTTP POST запрос
request = urllib2.Request(url, data)
time.sleep(3)

# Аргументы запроса, которые хотим отправить
query_args = { 'm':'10', 's':'' }

# Производим urlencodes для query_args
data = urllib.urlencode(query_args)

# Отправляем HTTP POST запрос
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
html = response.read()

# Выводим результат
print html

url = 'http://' + hostname + '/pgm/upload'

c = pycurl.Curl()
c.setopt(pycurl.URL, url)
b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.setopt(pycurl.POST, 1)
filesize = os.path.getsize(hexfname)
c.setopt(pycurl.POSTFIELDSIZE, filesize)
fin = open(hexfname, 'rb')
c.setopt(pycurl.READFUNCTION, fin.read)
c.perform()

response_code = c.getinfo(pycurl.RESPONSE_CODE)
response_data = b.getvalue()
c.close()
b.close()
print response_code
print response_data

