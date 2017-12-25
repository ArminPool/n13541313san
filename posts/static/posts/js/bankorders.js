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






    });
