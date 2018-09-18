# -*- coding: utf-8 -*-
import requests
import time
import sys
import telnetlib

hostname = str(input("Введите имя хоста или ip: "))

if hostname == '':
    hostname = '192.168.31.12' # Переменная ip адрес
    print('Имя хоста установлено: ' + hostname)

try:
    tn = telnetlib.Telnet(hostname, 23, 3)
except:
    print('Нет коннекта с ' + hostname)
    sys.exit(0)
tn.close()
print('Устройство ' + hostname +' доступно.')
tn.close()
time.sleep(1)


hexfname = str(input("Последняя прошивка Aqua73.hex.\n Если хотите другую прошивку введите имя файла *.hex: "))

if hexfname == '':
    hexfname = 'Aqua73.hex'  # Пременная имя файла
    print('Имя файла прошивки установлено: ' + hexfname)

url = 'https://hi-garden.ru/images/Flash/' + hexfname
#print(url)

try:
    r = requests.get(url, stream=True)
except requests.exceptions.ConnectionError:
    print('Нет подключения к сайту.')
    sys.exit(0)

try:
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    print('Ошибка загрузки прошивки с сайта.')
    sys.exit(0)
    
myhexd = (r.content)
if len(myhexd) < 2000:
    print('Не удалось найти прошивку на сайте или она повреждена') 
    sys.exit(0)
else:
    print('Прошивка на сайте имеется\n')

url = 'http://' + hostname + '/pgm/sync'

# POST запрос - сброс uC AQUARIUS
print('Сброс Aquarius для перепрошивки\n')
r = requests.post(url)

time.sleep(2)
#print(r.status_code)

# GET запрос туда же - чтение результата
try:
    r = requests.get(url)
except requests.exceptions.ConnectionError:
    print('Контроллер не отвечает после сброса...')

if r.status_code != 200:
    print(r.status_code)
    print('\nКонтроллер долго не отвечает!\n')
else:
    print(r.text)

# POST запрос - загрузка файла
url = 'http://' + hostname + '/pgm/upload'

r = requests.post(url, data = myhexd)
print(r.text)

if r.status_code != 200:
    print(r.status_code)
    print('\nОшибка перепрошивки!\n')
else:
    print('\nПерепрошивка прошла успешно!\n')

input()
