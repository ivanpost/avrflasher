<?php
$hostname = '192.168.31.12';
$hexfname = 'Blink2.hex';

$url = "http://" . $hostname . "/pgm/sync";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,$url);
curl_setopt($ch, CURLOPT_HEADER, 0); // нечитать заголовок
curl_setopt($ch, CURLOPT_TIMEOUT, 10);        // таймаут ответа
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, 's');

$result = curl_exec($ch);
if ($result === FALSE) {
    echo "cURL Error: " . curl_error($ch);
}
  
sleep(3);
curl_setopt($ch, CURLOPT_POST, 0);  

$result = curl_exec($ch);
if ($result === FALSE) {
    echo "cURL Error: " . curl_error($ch);
}

curl_close($ch);
echo " Res: " . $result . "  ";

// ===============

$url = 'http://localhost/upload_output.php';
//$url = 'http://' . $hostname . '/pgm/upload';


$post_data = array(
    // "foo" => "bar",
    // файл, который необходимо загрузить
	'd' => '@' . $hexfname
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);  // таймаут ответа
curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);

$result = curl_exec($ch);
curl_close($ch);
echo print_r($result);








?>