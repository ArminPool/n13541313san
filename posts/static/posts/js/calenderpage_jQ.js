$(document).ready(function() {


   $(document).ready(function(){


    if($('#main').height() < 340 ){


    $('footer').css('position','absolute');
     $('footer').css('bottom','0px');
    }
    else{
    }

$(window).on('resize', function(){

   if($('#main').height() < 340 ){


    $('footer').css('position','absolute');
     $('footer').css('bottom','0px');
    }


else{

 $('footer').css('position','relative');
}

});








$(window).on('resize', function(){

   if($('#main').height() < 340 ){


    $('footer').css('position','absolute');
     $('footer').css('bottom','0px');
    }


else{

 $('footer').css('position','relative');
}

});





$("footer").css("bottom","0px");
var d = new Date();
var month = d.getMonth()+1;
var day = d.getDate();
var date = d.getFullYear() + '-' +
    ((''+month).length<2 ? '0' : '') + month + '-' ;
 $.get("/economicCalendar/?q="+ date, function(data, status){
            $("#result").html(data);



        });

    $('[data-toggle="datepicker"]').datepicker({
  format: 'yyyy-mm-dd'
})
$("#input-picker").on("change paste keyup", function() {
    date = $(this).val();



        $.get("/economicCalendar/?q="+ date, function(data, status){
            $("#result").html(data);



        });

    });




    });
