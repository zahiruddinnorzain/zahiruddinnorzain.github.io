<?php

$id_series = strval($response["id"]);

$url = 'https://download.epizy.my.id/api/get/stream?series_id_list_episode='.$id_series;

if($response["id"] != ''){
    $response_episode = file_get_contents($url);
    $response_episode = json_decode($response_episode, true);
}
// print_r($response_episode);
foreach($response_episode as $list){
    // echo $list['id'];
    echo '<a href="https://download.epizy.my.id/series_area.php?id='.$response["id"].'&genre=Series&season='.$list['series_season'].'&episode='.$list['series_episode'].'" class=" mb-2 btn btn-sm btn-info">Season '.$list['series_season'].' Episode '.$list['series_episode'].'</a><br>';
}

?>