$(document).ready(function(){
    $("#logo" ).click(function(){
        $(location).attr('href', '/')
    });
    $("#facebook").click(function(){
        $(location).attr('href', 'https://www.facebook.com/Stubhub/')
    });
    $("#instagram").click(function(){
        $(location).attr('href', 'https://www.instagram.com/stubhub/')
    });
    $("#twitter").click(function(){
        $(location).attr('href', 'https://twitter.com/StubHub/')
    });
});