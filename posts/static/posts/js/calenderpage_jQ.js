$(document).ready(function() {


$("footer").css("bottom","0px");
var date = d.getFullYear() + '-' +
    ((''+month).length<2 ? '0' : '') + month + '-' ;
 $.get("/economicCalendar/?q="+ date, function(data, status){
            $("#result").html(data);
                        $(".date-header").css("display","none");
                         $(".date-column").css("display","none");


        });

    $('[data-toggle="datepicker"]').datepicker({
  format: 'yyyy-mm-dd'
})
$("#input-picker").on("change paste keyup", function() {
    date = $(this).val();



        $.get("/economicCalendar/?q="+ date, function(data, status){
            $("#result").html(data);
                        $(".date-header").css("display","none");
                         $(".date-column").css("display","none");


        });

    });




    });
