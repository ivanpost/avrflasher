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





echo "<p style='color: green'>Ожидание устройства</p><p style='color: green'>".$number_of_post." циклов синхронизации устройства с задержкой в ".$seconds." секунд. Ожидайте</p>";

// собираем echo в одну переменную, чтобы потом не вычищать вывод
$echo ="";



// технические переменные
$gotcha = true;
$programm = false;

// запрос на синхронизацию с устройством, при возврате SYNC - можно программировать
$url = 'http://'.$ip.'/pgm/sync';


$http_headers = array('Content-Type: text/plain');
    
// пытаемся достучаться до устройства, чтобы залить прошивку
while ($gotcha) 
{
            
    
            // первый запрос - post на синхронизацию
            senddata($url,$http_headers); 

            // второй запрос - get на проверку работы синхронизации, если в body вернуло SYNC - успех
            // если нет - идем на новый цикл
            $return = senddata($url,$http_headers,"get");

            $rest = mb_substr($return, 0, 4);
                
            if ($rest != "SYNC")
                    $echo.= "<p style='color: brown'>Устройство не готово</p>";
            else
                {
                        $echo.= "<p style='color: green'>Устройство синхронизировано</p>";

                        $gotcha = false;
                        $programm = true;
                }
    
    
    
    
    $number_of_post--;
    
    if ($number_of_post>0)
        $gotcha = false;
    
    
sleep($seconds);
} 

// если получена синхронизация - можно программировать
if ($programm)
{
    
        // делаем замер времени для того чтобы понять сколько грузится файл
        $time_start = microtime(true);

        $url = 'http://'.$ip.'/pgm/upload';
        $http_headers = array('Content-Type: text/plain');


        $echo.="<p style='color: green'>Начало процесса прошивки</p>";
    
        // заливаем файл на устройство
        $return = senddata($url,$http_headers,"post",$string);
    
        $echo.="<p>Сообщение от устройства: ".$return."</p>";
        
        // окончание замера времени
        $time_end = microtime(true);

        $time = $time_end - $time_start;

        // определяем получилось ли прошить, ищем в строке Success
            $pos = strpos($return,"Success");
        
            if ($pos===false)
                            $echo.="<p style='color: brown'>Ошибка при перепрошивке";    
                                    else
                                        $echo.="<p style='color: green'>Устройство перепрошито";    


            $echo.="<p style='color: green'>Время отправки файла: ".round($time,2)."c";


}
else 
    $echo.="<p style='brown'>Повторите еще раз, устройство не готово</p>";
    

// конечный вывод сообщений - можно отключить
echo  $echo;



// определение размера файла прошивки для загрузки методом безопасным для бинарников
// функции fread нужно передать точный размер файла

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

// функция проверки доступности ip

function availableUrl($host, $port=80, $timeout=5) { 
  $fp = fSockOpen($host, $port, $errno, $errstr, $timeout); 
  return $fp!=false;
}


// отправщик запросов и файла прошивки на устройство

function senddata($url,$http_headers,$method="post",$file=false)
{
    
            
                
            $ch = curl_init();
            // установка url
            curl_setopt($ch, CURLOPT_URL, $url);
            
            // установка http заголовка
            curl_setopt ($ch, CURLOPT_HTTPHEADER,$http_headers);
             
            // установка метода запроса
            if ($method=="post")
                curl_setopt($ch, CURLOPT_POST, 1);
                    else
                        curl_setopt($ch, CURLOPT_POST, 0);
            
    
            // установка тела запроса
            if ($file)    
                curl_setopt($ch, CURLOPT_POSTFIELDS, $file);

            // возврат строки весто прямого вывода в браузер
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        
            $intReturnCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            
            $response = curl_exec($ch);
                
                $err     = curl_errno( $ch );
                $errmsg  = curl_error( $ch );
                $header  = curl_getinfo( $ch); 

                curl_close($ch);

    // раскоментировать для дебага заголовоков
//echo "<p>Сервер вернул: </p>";
//    var_dump($response);

//    echo "<p>Хедер</p>";
//    print_r($header);
//    echo "<p>Ошибки запроса</p>";
//    print_r($err);
//    print_r($errmsg);   
    return $response;
}



    
    
?>