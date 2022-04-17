<?php
stream_context_set_default( [
    'ssl' => [
        'verify_peer' => false,
        'verify_peer_name' => false,
    ],
]);

//input
$input = $_GET["input"];

// TIMEZONE
date_default_timezone_set("Asia/Kuala_Lumpur");

//date
$date = date("l - d/m/Y H:i:s");
$masej = '';


if($input == 'emassilver'){

    $data = file_get_contents('https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD');
    $data = json_decode($data, true);
    // var_dump( $data[5]['spreadProfilePrices'][1]['bid'] );
    $data = $data[5]['spreadProfilePrices'][1]['bid'];

    $masej = 'Mula+Meniaga %0A'.'Silver+dan+Emas: %0A'.'+'.$date.'+%0A %0A+'.$data;
    // echo $masej;

    $output_init = file_get_contents('https://api.telegram.org/bot2041486796:AAHe5rC_HQ64jCjXw6TgYx__W3pdp8OI4GE/sendMessage?chat_id=-1001540152981&text='.$masej);


}elseif($input == 'minyak'){

    $masej = 'Mula+Meniaga+WTI Crude Oil';
    // echo $masej;

    $output_init = file_get_contents('https://api.telegram.org/bot2041486796:AAHe5rC_HQ64jCjXw6TgYx__W3pdp8OI4GE/sendMessage?chat_id=-1001540152981&text='.$masej);

}else{
    echo 'error';
}


?>
