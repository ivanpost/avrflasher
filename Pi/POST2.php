<?php
$ch = curl_init();

$file = "Blink2.hex";
$url = 'http://localhost/upload_output.php';
$lenfile = filesize($file);
echo " LEN FILE: " . $lenfile . "  ";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);  // таймаут ответа
$fp = fopen($file, "rb");
curl_setopt($ch, CURLOPT_INFILE, $fp);
curl_setopt($ch, CURLOPT_INFILESIZE, $lenfile);

$result = curl_exec($ch);
if ($result === FALSE) {
    echo "cURL Error: " . curl_error($ch);
}
curl_close($ch);
echo $result;







?>