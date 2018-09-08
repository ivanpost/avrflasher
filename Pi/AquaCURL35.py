# -*- coding: cp1251 -*-
import pycurl
import io
import time
import os.path

hostname = '192.168.31.12' # ���������� ip �����
hexfname = 'Blink1.hex'  # ��������� ��� �����

url = 'http://' + hostname + '/pgm/sync'

# POST ������ - ����� uC AQUARIUS
print('Resetting Aquarius\n')
b = io.BytesIO()
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.TIMEOUT, 10)
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.setopt(pycurl.POSTFIELDS, 's')
c.perform()

time.sleep(3)

# GET ������ ���� �� - ������ ����������
c.setopt(pycurl.POST, 0)
c.perform()

# ����� ����������
response_data = b.getvalue()
c.close()
print(response_data)

url = 'http://' + hostname + '/pgm/upload'

# POST ������ - �������� �����
print('\nUpload flash file in Aquarius\n')
b = io.BytesIO()
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

# ����� ����������
response_data = b.getvalue()
b.close()
c.close()
print(response_data)
