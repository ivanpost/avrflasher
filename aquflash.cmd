@echo off
set /p ipnum=Aquarius ip or hostname: 
echo %ipnum%

ping -n 2 -w 500 %ipnum%

echo Upload file from hi-garden.ru

set "str4=http://%ipnum%/pgm/sync"
set "str5=http://%ipnum%/pgm/upload"
set "str6=@Aqua73.hex"

curl -m 20 -O https://hi-garden.ru/images/Flash/Aqua73.hex
echo Reset Aquarius.
curl -m 10 -s -XPOST %str4%
ping -n 1 -w 1500 10.10.254.254 >nul
curl -m 15 -s %str4%
echo Flashing Aquarius.
echo.
curl -m 15 -s -g -d %str6% %str5%
pause
exit


:error1
echo Aquarius IP or host need!
pause
exit
