
/* NFORMATION

wikipedia_api('<person of interest>','<language>','<tag id html>');

=================================================================================
EXAMPLE:
<script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
<script src="https://zahiruddinnorzain.github.io/wikipedia-api.js"></script>

<p id="wiki"></p>

<script>
var result = wikipedia_api('mahathir mohamad','ms','wiki');
</script>
=================================================================================
by kepaknaga@gmail.com

*/

function wikipedia_api(nama,lang,tag_id)
{
    $.ajax({
        url: `https://${lang}.wikipedia.org/w/api.php?action=query&format=json&list=search&origin=*&srsearch=${nama}`,
        type: "GET",
        async: false,
        success: function (response) {
            wikiwiki_api_show(response.query.search[0].pageid,lang,tag_id)
        }
    });
}

function wikiwiki_api_show(page_id,lang,tag_id)
{
    $.ajax({
        url: `https://${lang}.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&origin=*&pageids=${page_id}&redirects=1&formatversion=2`,
        type: "GET",
        async: false,
        success: function (response) {
            result = response.query.pages[0].extract
            $('#'+tag_id).html(result)
        }
    });
}