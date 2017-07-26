$(document).ready(function(){

    $( "#number" )
      .selectmenu()
      .selectmenu( "menuWidget" )
        .addClass( "overflow" );

    
    $("#logo").click(function(){
      $(location).attr('href', '/')
    });

});