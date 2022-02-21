<?php

$status_epizymovie = '';
$status_api = '';

stream_context_set_default( [
    'ssl' => [
        'verify_peer' => false,
        'verify_peer_name' => false,
    ],
]);

// TIMEZONE
date_default_timezone_set("Asia/Kuala_Lumpur");

// CHECK API
$check_api = get_headers('https://download.epizymovie.my.id/', 1);

if ($check_api[0] != 'HTTP/1.1 200 OK') {
    $status_api = 'API_404_ERROR';
}else{
    $status_api = 'API_ONLINE_OK';
}

// CHECK WEBSITE
$check_epizymovie = get_headers('http://epizymovie.my.id/', 1);

if ($check_epizymovie[0] != 'HTTP/1.1 200 OK') { 
    $status_epizymovie = 'WEBSITE_404_ERROR';
}else{
    $status_epizymovie = 'WEBSITE_ONLINE_OK';
}

//date
$date = date("l - d/m/Y H:i:s");

$masej = 'SERVER+REPORT: %0A'.'+'.$date.'+%0A %0A+'.$status_api.'+%0A+'.$status_epizymovie;
// echo $masej;

$output_init = file_get_contents('https://api.telegram.org/bot2041486796:AAHe5rC_HQ64jCjXw6TgYx__W3pdp8OI4GE/sendMessage?chat_id=-1001540152981&text='.$masej);

?>

<!DOCTYPE html>
<html lang="en">
<head>
<title>epizyMovie server info</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="hhttps://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.min.js"></script> -->
</head>
<body>

<?php
echo($date.'<br>');
echo($status_api.'<br>');
echo($status_epizymovie.'<br>');
?>


</body>
</html>
