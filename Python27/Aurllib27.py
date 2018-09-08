#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
import pycurl
import StringIO
import os.path

# hexfile = urllib2.urlopen("https://hi-garden.ru/images/Flash/Aqua73.hex")

# output = open('Aqua73.hex','wb')
# output.write(hexfile.read())
# output.close()

# Данные, которые хотим отправить
query_args = { 'm':'10', 's':'', 'X':'' }

# Производим urlencodes для ранее созданного словаря (вот для чего мы импортировали библиотеку urllib вверху)
data = urllib.urlencode(query_args)

# Отправляем HTTP POST запрос
request = urllib2.Request('http://192.168.31.12/pgm/sync', data)

time.sleep(2)

# Данные, которые хотим отправить
query_args = { 'm':'10', 's':'' }

# Производим urlencodes для ранее созданного словаря (вот для чего мы импортировали библиотеку urllib вверху)
data = urllib.urlencode(query_args)

# Отправляем HTTP POST запрос
request = urllib2.Request('http://192.168.31.12/pgm/sync', data)

response = urllib2.urlopen(request)

html = response.read()

# Выводим результат
print html


def main():
 
    method = 4
    filename = 'Blink1.hex'
    url = 'http://192.168.31.12/pgm/upload'

    c = pycurl.Curl()
    c.setopt(pycurl.VERBOSE, 1)
    c.setopt(pycurl.URL, url)
    fout = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, fout.write)

    if method == 1:
        c.setopt(pycurl.HTTPPOST, [
                ("file1",
                 (c.FORM_FILE, filename))])
        c.setopt(pycurl.HTTPHEADER, [''])
    elif method == 2:
        c.setopt(c.HTTPPOST, [
                ("uploadfieldname",
                 (c.FORM_FILE, filename,
                  c.FORM_CONTENTTYPE, ""))])
    elif method == 3:
        c.setopt(pycurl.UPLOAD, 1)
        c.setopt(pycurl.READFUNCTION, open(filename, 'rb').read)
        filesize = os.path.getsize(filename)
        c.setopt(pycurl.INFILESIZE, filesize)
    elif method == 4:
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.HTTPHEADER, [''])
        filesize = os.path.getsize(filename)
        c.setopt(pycurl.POSTFIELDSIZE, filesize)
        fin = open(filename, 'rb')
        c.setopt(pycurl.READFUNCTION, fin.read)

    c.perform()
    response_code = c.getinfo(pycurl.RESPONSE_CODE)
    response_data = fout.getvalue()
    print response_code
    print response_data
    c.close()


if __name__ == '__main__':
    main()
