<?php

$id = $_GET["id"];
$genre = $_GET["genre"];
$season = $_GET["season"];
$episode = $_GET["episode"];
$option = $_GET["option"];

if(($id != '') && ($genre != '')){
    $response = file_get_contents('https://download.epizymovie.my.id/api/get/stream?id='.$id.'&genre='.$genre.'&season='.$season.'&episode='.$episode);
    // $response = file_get_contents('http://localhost:8000/api/get/stream?id=2');
    $response = trim($response, '"[]"');
    $response = json_decode($response, true);
}

// http://localhost:3000/movie_area.php?id=5&option=2

?>

<!DOCTYPE html>
<html lang="en">
<head>
<title>epizyMovie</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="hhttps://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.min.js"></script>
</head>
<body>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
body {
  margin: 0;
  font-family: Poppins, Arial, Helvetica, sans-serif;
  background-color: #000;
  color: #ddd;
}
.share .fa {
	padding: 15px;
	font-size: 20px;
	text-align: center;
	text-decoration: none;
	margin: 5px 2px;
	border-radius: 100px;
	height: 100%;
	width: 50px;
	box-shadow: 1px 0px 10px black;
}

.fa:hover {
	opacity: 0.7;
}

.fa-facebook {
	background: #514DB5;
	color: white;
}
.fa-twitter {
	background: #55ACEE;
	color: white;
}
.fa-instagram {
	background: #125688;
	color: white;
}
.fa-youtube {
	background: #bb0000;
	color: white;
}
.fa-google {
	background: #dd4b39;
	color: white;
}
</style>

<nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #000;">
	<a class="navbar-brand" href="https://epizymovie.my.id/">epizyMovie</a>
	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
		<span class="navbar-toggler-icon"></span>
	</button>
	<div class="collapse navbar-collapse" id="navbarNav">
		<ul class="navbar-nav">
			<li class="nav-item active">
				<a class="nav-link" href="#">Home</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="#">Features</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="#">Join Club</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="#">About Us</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="#">Movie Suggestion</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="#">Remove Ads</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="#">Report Issue</a>
			</li>
		</ul>
	</div>
</nav>

<div class="row mr-0">
        <div class="col-sm-12">

            <div class="card p-2 my-2" style="margin-left:0px;margin-right:0px;background-image:url('http://epizymovie.my.id/n3.gif');">

                <h2 style="font-family: lucida handwriting;color:rgba(255, 195, 0.9);"><b>epizyMovie</b></h2>
                <marquee behavior="scroll" direction="left" scrollamount="10"><b style="color: white;">Kami akan update dari masa ke semasa dan jangan lupa share Link ini okey</b></marquee>
                <h3 class="">
                    <span class="text-wrapper">
                    <span class="letters">Series Area</span>
                    </span>
                </h3>

                <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js"></script>

            </div>

        </div>

        <div class="col-sm-2"></div>

        <div class="col-sm-8">

            <div class="card bg-dark">
                <center>
                    <div class="" style="color: white;" style="text-align: center;"><h3 style="text-shadow: 8px 8px 8px #000;">Trailer: <?php echo $response["stream_tajuk"] ?></h3>
                        <div class="videowrapper">
                            <iframe width="640px" height="480px" src="<?php echo $response["stream_trailer_embedcode"] ?>" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                            </iframe>
                        </div>
                    </div>

                    <p>Season & Episode</p>
                    <?php

                        $id_series = strval($response["id"]);

                        $url = 'https://download.epizymovie.my.id/api/get/stream?series_id_list_episode='.$id_series;

                        if($id_series != ''){
                            $response_episode = file_get_contents($url);
                            $response_episode = json_decode($response_episode, true);
                        }
                        // print_r($response_episode);
                        foreach($response_episode as $list){
                            // echo $list['id'];
                            echo '<a href="http://epizymovie.my.id/series_area.php?id='.$response["id"].'&genre=Series&season='.$list['series_season'].'&episode='.$list['series_episode'].'" class=" mb-2 btn btn-sm btn-info">Season '.$list['series_season'].' Episode '.$list['series_episode'].'</a><br>';
                        }

                    ?>

                </center>
            </div>

        </div>

        <div class="col-sm-2"></div>

        <div class="col-sm-12">
            <div class="card bg-dark mt-2 mb-4">
                <div class="movietitle" style="color: white;" style="text-align: center;"><h4 style="text-shadow: 8px 8px 8px #000;"><b>SERIES Title: <?php echo $response["stream_tajuk"] ?>, S<?php echo $response["series_season"] ?>E<?php echo $response["series_episode"] ?> </b></h4>
                </div>
                
                <center>
                    <div class="videowrapper">
                        <iframe id="iframe_movie" width="100%" height="500px" src="<?php echo $response["series_embed"] ?>" allowfullscreen allowtransparency allow="autoplay" scrolling="no" frameborder="0" ></iframe>
                    </div>
                </center>

                <div class="fa mb-2" style="margin-top: 10px;padding: 5px;background-color: grey;color: white;border-radius: 10px;font-weight: 100px;opacity: 0.5;width:210px"> Click '&#xf013;' to open subtitle </div>
            </div>
        </div>

        <div class="col-sm-12">
            <h3 style="color: white;margin-left: 10px;">Comment</h3>
            <div id="disqus_thread" style="margin-left: 20px;margin-right: 20px;border-radius: 10px;"></div>
            <script>
                /**
                *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
                *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables    */
                
                var disqus_config = function () {
                this.page.url = 'http://epizymovie.my.id/';  // Replace PAGE_URL with your page's canonical URL variable
                this.page.identifier = <?php echo $response["stream_tajuk"] ?>; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
                };
                
                (function() { // DON'T EDIT BELOW THIS LINE
                var d = document, s = d.createElement('script');
                s.src = 'https://epizymovie-1.disqus.com/embed.js';
                s.setAttribute('data-timestamp', +new Date());
                (d.head || d.body).appendChild(s);
                })();
            </script>
        </div>
        

</div>

        
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
<footer class="page-footer " style="background-color: black;">
    <div class="titlefooter" style="color: grey;font-size: 1.2em;text-align: center;">Follow us on</div>	
        <div class="share" style="text-align: center;">   
            <a href="https://www.google.com" style="color: black;"><i class="fa fa-google"></i></a>
            <a href="https://www.facebook.com" style="color: black;"><i class="fa fa-facebook"></i></a>
            <a href="https://www.instagram.com" style="color: black;"><i class="fa fa-instagram"></i></a>
            <a href="https://www.youtube.com" style="color: black;"><i class="fa fa-youtube"></i></a>
            <a href="https://www.twitter.com" style="color: black;"><i class="fa fa-twitter"></i></a>
        </div>
    <!-- Copyright -->
    <div class="footer-copyright text-center py-3 text-secondary">© 2021 Copyright
    <p class="text-secondary">Created by: Areyip</p>
    </div>
    <!-- Copyright -->
</footer>

</body>
</html>