#!python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import time
import telnetlib
import sys

hostname = str(input('Введите имя хоста или ip: '))

if hostname == '':
    hostname = '192.168.31.12' # Переменная ip адрес
    print('Имя хоста установлено: ' + hostname)

try:
    tn = telnetlib.Telnet(hostname, 23, 3)
except:
    print('Нет коннекта с ' + hostname)
    sys.exit(0)
tn.close()

print('Устройство ' + hostname + u' доступно.')
tn.close()
time.sleep(1)

print('Последняя прошивка Aqua73.hex.\nЕсли хотите другую прошивку введите имя файла')
hexfname = str(input( '*.hex: '))

if hexfname == '':
    hexfname = 'Blink1.hex'  # Пременная имя файла
    print('Имя файла прошивки установлено: ' + hexfname)

url = 'https://hi-garden.ru/images/Flash/' + hexfname
hexfile = urllib.request.urlopen(url)
#print(hexfile.read())

'''
try:
    hexfile = urllib.request.urlopen(url)
except urllib2.HTTPError as e:
        print('HTTP ошибка. Неподходящий файл.')
        sys.exit(0)
except urllib2.URLError as e:
        print('URL ошибка. Нет доступа к файлу.')
        sys.exit(0)


url = 'http://' + hostname + '/pgm/sync'

# Аргументы запроса, которые хотим отправить
query_args = { 's':'' }

# Производим urlencodes для query_args
data = urllib.parse.urlencode(query_args)

# Отправляем HTTP POST запрос
request = urllib.request.Request(url, data)
response = urllib.request.urlopen(request)

time.sleep(2)

request = urllib2.urlopen(url)
print(request.read())

url = 'http://' + hostname + '/pgm/upload'

request = urllib.request.Request(url, hexfile.read())
response = urllib.request.urlopen(request)

print(response.read())
'''
