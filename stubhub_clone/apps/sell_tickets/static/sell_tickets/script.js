

$(document).ready(function (){

    $("#ex1").slider({
	    formatter: function(value) {
            $("#show-price").text(value)
	    }
    });



    // $('#searchIcon').click(function(){
    //     $('#hide-this').show();
    //     $('#sell-search-form').submit();
    // });


    $("#selection").click(function(){
        $("#secret-price").show();
    });

    $(".slider-handle").click(function(){
        $("#secret-seats").show();
    });

    $(".display-create").click(function(){
        $("#make-listing").show();
    });

    $("#make-listing").click(function(){
        $("#submit-listing").submit(function(e){
            e.preventDefault();
        });
        swal("Thank you!", "Your listing has been created.", "success");
        $(".confirm").click(function(){
            $("#submit-listing").unbind('submit').submit();
        });
    });
        
});