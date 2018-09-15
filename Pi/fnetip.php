<?
// установка кодировки utf-8
mb_internal_encoding("UTF-8");

//увеличение времени работы скрипта до 5ти минут
ini_set('max_execution_time', 300);


error_reporting(E_ERROR | E_PARSE);

//проверка на существование библиотеки curl
try 
{
    if (!function_exists('curl_init'))
        throw new Exception("curl не работает");
}
catch (Exception $e) {
    // код который может обработать исключение
    echo $e->getMessage();
    die;
}

//
//КОНФИГРУАЦИЯ
//


//ip устройства и ссылка на файл прошивки
$ip = "192.168.31.12";
$file_url = 'https://hi-garden.ru/images/Flash/BlinkUno.hex';

// сколько запросов на синхронизацию с устройством будет сделано
$number_of_post = 10;

// сколько секунд ждать между запросами
$seconds = 1;



//проверяем наличие ip устройства в сети 
try 
{
   
    if (availableUrl($ip)==false)
        throw new Exception("Устройство c ip адресом: ".$ip." недоступно");
}
catch (Exception $e) {
    // код который может обработать исключение
    echo $e->getMessage();
    die;
}

echo "<p style='color: green'>Ожидание устройства</p><p style='color: green'>";

function availableUrl($host, $port=80, $timeout=5) { 
  $fp = fSockOpen($host, $port, $errno, $errstr, $timeout); 
  return $fp!=false;
}

    
?>