# -*- coding: utf-8 -*-
import requests
import io
import time
import os.path
import sys
from contextlib import closing

hostname = '192.168.31.12' # Переменная ip адрес
hexfname = 'Blink1.hex'  # Пременная имя файла

url = 'https://hi-garden.ru/images/Flash/' + hexfname
print(url)

try:
    r = requests.get(url, stream=True)
except requests.exceptions.ConnectionError:
    print('Conn error')
    exit.sys(0)

myhexd = (r.content)


url = 'http://' + hostname + '/pgm/sync'

# POST запрос - сброс uC AQUARIUS
print('Resetting Aquarius\n')
r = requests.post(url)


time.sleep(2)
print(r.status_code)

# GET запрос туда же - чтение результата
r = requests.get(url)
print(r.status_code)
print(r.text)


url = 'http://' + hostname + '/pgm/upload'

r = requests.post(url, data = myhexd)
print(r.status_code)
print(r.text)

# POST запрос - загрузка файла
print('\nUpload flash file in Aquarius\n')


