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
$file_url = 'https://hi-garden.ru/images/Flasht/Blink1.hex';

// сколько запросов на синхронизацию с устройством будет сделано
$number_of_post = 10;

// сколько секунд ждать между запросами
$seconds = 1;

//сюда сохранится прошивка
$string ="";



//открываем файл в бинарном виде и сохраняем в стороковую переменную для передачи
try 
{
   $file_size = fsize($file_url);

    $fh = fopen($file_url,"r");
    $string = fread($fh,$file_size);
    fclose($fh);
    
    if ($fh==false)
        throw new Exception("Неправильная ссылка на файл прошивки");
}
catch (Exception $e) {
    // код который может обработать исключение
    echo $e->getMessage();
    die;
}

echo $string;

function fsize($path)
{
    $fp = fopen($path,"r");
    $inf = stream_get_meta_data($fp);
    fclose($fp);
    foreach($inf["wrapper_data"] as $v)
    if (stristr($v,"content-length"))
            {
            $v = explode(":",$v);
            return trim($v[1]);
            }
}    
    
?>