$(document).ready(function() {


$("footer").css("bottom","0px");
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
