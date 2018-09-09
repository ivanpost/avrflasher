<?php
$hostname = '192.168.31.12';
$hexfname = 'Blink2.hex';

$ch = curl_init();
$url = "http://" . $hostname . "/pgm/sync";
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

//$url = 'http://localhost/upload_output.php';
$url = 'http://' . $hostname . '/pgm/upload';

$lenfile = filesize($hexfname);
echo " LEN FILE: " . $lenfile . "  ";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);  // таймаут ответа
$fp = fopen($hexfname, "rb");
curl_setopt($ch, CURLOPT_INFILE, $fp);
curl_setopt($ch, CURLOPT_INFILESIZE, $lenfile);

$result = curl_exec($ch);
if ($result === FALSE) {
    echo "cURL Error: " . curl_error($ch);
}
curl_close($ch);
echo $result;







?>