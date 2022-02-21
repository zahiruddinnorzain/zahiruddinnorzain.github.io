// <script src="https://cdn.rawgit.com/zahiruddinnorzain/zahiruddinnorzain.github.io/master/dist/dummy/profile_dummy.js"></script>

var dummy = {
    "profile": { 
        "nama":"ZAHIRUDDIN",
        "nama_bapa":"NORZAIN",
        "phone":"0171233234",
        "email":"emailsaya@gmailm.com",
        "alamat_1":"No.2, jalan 5",
        "poskod":"48000",
        "negeri":"Selangor",
        "negara":"Malaysia",
        "jantina":"Lelaki",
        "poskod":"48000",
    }
};

$(document).ready(function(){

    // console.log(dummy["profile"]["nama"]);
    $('#noLaporan').val(dummy["profile"]["nama"]);
    $('#nama').val(dummy["profile"]["nama"]);
    $('#phone').val(dummy["profile"]["phone"]);
    $('#email').val(dummy["profile"]["email"]);
    $('#alamat_1').val(dummy["profile"]["alamat_1"]);
    $('#poskod').val(dummy["profile"]["poskod"]);
    $('#negeri').val(dummy["profile"]["negeri"]);
    $('#negara').val(dummy["profile"]["negara"]);
    $('#jantina').val(dummy["profile"]["jantina"]);

});