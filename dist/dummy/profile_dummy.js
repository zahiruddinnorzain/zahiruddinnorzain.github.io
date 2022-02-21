// <script src="https://cdn.rawgit.com/zahiruddinnorzain/zahiruddinnorzain.github.io/master/dist/dummy/profile_dummy.js"></script>

var dummy = {
    "profile": { 
        "nama":"ZAHIRUDDIN",
        "nama_bapa":"NORZAIN",
        "phone":"0171233234",
        "email":"emailsaya@gmailm.com",
    }
};

$(document).ready(function(){

    // console.log(dummy["profile"]["nama"]);
    $('#noLaporan').val(dummy["profile"]["nama"]);
    $('#nama').val(dummy["profile"]["nama"]);
    $('#phone').val(dummy["profile"]["phone"]);
    $('#email').val(dummy["profile"]["email"]);

});