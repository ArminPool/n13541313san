$(document).ready(function() {


$("footer").offset.bottom = 0;
    $('[data-toggle="datepicker"]').datepicker({
  format: 'yyyy-mm-dd'
})
$("#input-picker").on("change paste keyup", function() {
    date = $(this).val();



        $.get("/EconomicCalendar/?q="+ date, function(data, status){
            $("#result").html(data);
                        $(".date-header").css("display","none");
                         $(".date-column").css("display","none");


        });

    });




    });
