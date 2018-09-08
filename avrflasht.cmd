@echo off
curl -m 20 -O -k https://hi-garden.ru/images/Aquarius/Aqua73.hex
curl -m 10 -s -XPOST http://192.168.31.12/pgm/sync
sleep(2)
curl -m 10 -s http://192.168.31.12/pgm/sync
echo.
curl -m 10 -s -g -d "@BlinkUno.hex" "http://192.168.31.12/pgm/upload"
pause
