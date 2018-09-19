#!/usr/bin/python2
# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
import pyping
import telnetlib
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

hostname = raw_input(u'Введите имя хоста или ip: ')

if hostname == '':
    hostname = '192.168.31.12' # Переменная ip адрес
    print u'Имя хоста установлено: ' + hostname

try:
    tn = telnetlib.Telnet(hostname, 23, 3)
except:
    print u'Нет коннекта с ' + hostname
    sys.exit(0)
tn.close()

print u'Устройство ' + hostname + u' доступно.'
tn.close()
time.sleep(1)


hexfname = raw_input(u"Последняя прошивка Aqua73.hex.\n Если хотите другую прошивку введите имя файла *.hex: ")

if hexfname == '':
    hexfname = 'Blink1.hex'  # Пременная имя файла
    print u'Имя файла прошивки установлено: ' + hexfname

url = 'https://hi-garden.ru/images/Flash/' + hexfname

try:
    hexfile = urllib2.urlopen(url)
except urllib2.HTTPError as e:
        print u'HTTP ошибка. Неподходящий файл.'
        sys.exit(0)
except urllib2.URLError as e:
        print u'URL ошибка. Нет доступа к файлу.'
        sys.exit(0)

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

