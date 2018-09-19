#!/usr/bin/python2
# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
#import StringIO
#import os.path
import pyping
import sys

hostname = '192.168.31.12' # Переменная ip адрес
hexfname = 'Blink1.hex'  # Пременная имя файла

r = pyping.ping(hostname)

if r.ret_code == 0:
    print "Ping " + hostname +" OK"
    time.sleep(1)
else:
    print "Sorry uC not response"
    sys.exit(0)

hexfile = urllib2.urlopen("https://hi-garden.ru/images/Flash/" + hexfname)


url = 'http://' + hostname + '/pgm/sync'

# Аргументы запроса, которые хотим отправить
query_args = { 's':'' }

# Производим urlencodes для query_args
data = urllib.urlencode(query_args)

# Отправляем HTTP POST запрос
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)

time.sleep(2)

request = urllib2.urlopen(url)
print request.read()

url = 'http://' + hostname + '/pgm/upload'

request = urllib2.Request(url, hexfile.read())
response = urllib2.urlopen(request)

print response.read()

