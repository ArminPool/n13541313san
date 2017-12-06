$(document).ready(function() {

var ScreenWidth = $(window).width();


if(ScreenWidth < 752){


$(".navbar-collapse").css("margin-right","0px");

}

$(window).on('resize', function(){


if($(this).width() != ScreenWidth){
if($(this).width() < 752){
$(".navbar-collapse").css("margin-right","0px");



}
else{


$(".navbar-collapse").css("margin-right","103px");




}
ScreenWidth = $(this).width();
}

});

$("input").focus(function(){
    $(this).prev('.fa').css("color", "#1E90FF");
    $(this).prev('.material-icons').css("color", "#1E90FF");

});

$("select").focus(function(){
    $(this).prev('.material-icons').css("color", "#1E90FF");

});

$("input").blur(function(){
    $(this).prev('.fa').css("color", "rgb(204, 204, 204)");
    $(this).prev('.material-icons').css("color", "rgb(204, 204, 204)");
});

$("select").blur(function(){
    $(this).prev('.material-icons').css("color", "rgb(204, 204, 204)");
});



$("input").focus(function(){
    $(this).css("border", "1px solid #1E90FF");
});

$("input").blur(function(){
    $(this).css("border", "1px solid rgb(204, 204, 204)");
});
 $(function(){
        $('input').blur();
        $('select').blur();
    });
});




