function list_html(arr){
        var html = "";
        for(var i = 0; i < arr.length; i+=1){
            html += "<div class='col-md-12 msg'>" + arr[i] + "</div>";
        }
        return html;
    }


$(document).ready(function(){

    $("#sign-up").click(function() {
        $("#choose-log").hide();
        $("#choose-reg").show();
    });

    $("#login-now").click(function() {
        $("#choose-reg").hide();
        $("#choose-log").show();
    });

    $("#login-form").submit(function(e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.
        var url = "/authenticate"; // the script where you handle the form input.
        $.ajax({
               type: "POST",
               url: url,
               data: $("#login-form").serialize(), // serializes the form's elements.
               dataType: "json",
               success: function(data)
               {
                   console.log(data);
                   var msgs = data.messages;
                   console.log(msgs);
                   if (data.fail == true){
                        $('#login-msg-placeholder').html(list_html(msgs));
                   } else {
                       $("#checkout-form").submit();
                    //    window.location.href = "/checkout/review";
                   }
               }
        });
    });

    $("#register-form").submit(function(e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.
        var url = "/register"; // the script where you handle the form input.
        $.ajax({
               type: "POST",
               url: url,
               data: $("#register-form").serialize(), // serializes the form's elements.
               dataType: "json",
               success: function(data)
               {
                   console.log(data);
                   var msgs = data.messages;
                   console.log(msgs);
                   if (data.fail == true){
                        $('#register-msg-placeholder').html(list_html(msgs));
                   } else {
                       $("#checkout-form").submit();
                    //    window.location.href = '/checkout/review';
                   }
               }
             });
    });
            
    $( "#number" )
      .selectmenu()
      .selectmenu( "menuWidget" )
        .addClass( "overflow" );

    
    $("#logo").click(function(){
      $(location).attr('href', '/')
    });

});