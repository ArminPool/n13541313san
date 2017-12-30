$(document).ready(function() {
closeNav();
var clicked;
$(".comments span + button").click(function(event){
    event.preventDefault();
    $(this).nextAll('form').first().fadeToggle();


});

$("#post-text p img").addClass('img-responsive');

$(".show-replies").click(function(event){
    event.preventDefault();
     $(this).nextAll('.see-replies').first().fadeToggle();

});
 $("textarea").before("<label>پیام</label>");


$('blockquote').filter(function(){return $(this).text().trim().length==0}).remove();

function closeNav(){

sideNav = 2;
var ScreenWidth = $(window).width();
if(ScreenWidth < 586){
$("footer").css("display","block");
$("#main").css("display","block");


$("#SideNav").css("width","0px");
$("#left-side-toggle-open").css("display","inline");

$("#left-side-toggle-close").css("display","none");

}
else{

$("footer").css("display","block");
$("#main").css("display","block");
$("#main").css("margin-right","0px");
$("#SideNav").css("width","0px");
$("#left-side-toggle-open").css("display","inline");

$("#left-side-toggle-close").css("display","none");

}

  }

});