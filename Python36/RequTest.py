# -*- coding: utf-8 -*-
import requests
import io
import time
import os.path
import sys

hostname = '192.168.31.12' # Переменная ip адрес
hexfname = 'BlinkUno.hex'  # Пременная имя файла

url = 'https://hi-garden.ru/images/Flash/' + hexfname
print(url)

try:
    r = requests.get(url)
except requests.exceptions.ConnectionError:
    print('Conn error')
    exit.sys(0)

myhexd = r.content
myhex = {'d' : ('myhex.hex', myhexd)}
print(myhex)

'''
url = 'http://' + hostname + '/pgm/sync'

# POST запрос - сброс uC AQUARIUS
print('Resetting Aquarius\n')
r = requests.post(url)
print(r.status_code)

time.sleep(2)

# GET запрос туда же - чтение результата
r = requests.get(url)

# Вывод результата
print(r.status_code)
print(r.content)
url = 'http://' + hostname + '/pgm/upload'


r = requests.post(url, files=myhex)
print(r.status_code)
print(r.content)

# POST запрос - загрузка файла
print('\nUpload flash file in Aquarius\n')
'''
