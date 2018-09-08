#!/bin/sh
#curl -m 20 -O "https://hi-garden.ru/images/Flash/Aqua73.hex"
#sleep 2
curl -m 10 -s -XPOST "http://192.168.31.12/pgm/sync"
sleep 1
curl -m 10 -s "http://192.168.31.12/pgm/sync"
curl -m 10 -s -g -d "@Aqua73.hex" "http://192.168.31.12/pgm/upload"