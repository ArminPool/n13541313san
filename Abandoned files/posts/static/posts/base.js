$(document).ready(function() {
    $(function(){
        $('input').blur();
    });
var sideNav;
var headerWidth = parseFloat($(".navbar-header").css("width")) ;


if( headerWidth > 97){

$(".navbar-header").css("padding-left","50px");
}
else{
$(".navbar-header").css("padding-left","0px");
}

var ScreenWidth = $(window).width();
if(ScreenWidth < 586){

$("#main").css("display","block");
$("#SideNav").css("width","0px");
}
else{
$("#main").css("margin-left","250px");
$("#SideNav").css("width","250px");
$("#left-side-toggle-open").css("display","none");
$("#left-side-toggle-close").css("display","inline");

}

$("#left-side-toggle-open").click(function(){


var ScreenWidth = $(window).width();
if(ScreenWidth < 586){
$("footer").css("display","none");
$("#main").css("display","none");
$("#SideNav").css("width","100%");
$("#left-side-toggle-open").css("display","none");

$("#left-side-toggle-close").css("display","inline");

}
else{
$("#main").css("display","block");
$("footer").css("display","block");
$("#main").css("margin-left","250px");
$("#SideNav").css("width","250px");
$("#left-side-toggle-open").css("display","none");

$("#left-side-toggle-close").css("display","inline");
}

});

var ScreenWidth = $(window).width();
$(window).on('resize', function(){
   if($(this).width() != ScreenWidth){


var headerWidth = parseFloat($(".navbar-header").css("width")) ;
var headerPadding = parseFloat($(".navbar-header").css("padding-left")) ;
if ($(this).width() > ScreenWidth){

if( (headerWidth - headerPadding) > 97 && (headerPadding > 0) ){


$(".navbar-header").css("padding-left","50px");
}
else{


$(".navbar-header").css("padding-left","0px");
}
}
else{
if((headerWidth - headerPadding) > 97){

$(".navbar-header").css("padding-left","50px");
}
}


if(ScreenWidth < 586){
$("#main").css("marginLeft","0px");
$("#SideNav").css("width","0px");
$("#left-side-toggle-open").css("display","none");
$("#main").css("display","block");
$("#left-side-toggle-close").css("display","inline");
}
else{

$("#main").css("display","block");
$("footer").css("display","block");
$("#main").css("marginLeft","250px");
$("#SideNav").css("width","250px");
$("#left-side-toggle-open").css("display","none");

$("#left-side-toggle-close").css("display","inline");

}
 ScreenWidth = $(this).width();
}



});




$("#left-side-toggle-close").click(function(){

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
$("#main").css("margin-left","0px");
$("#SideNav").css("width","0px");
$("#left-side-toggle-open").css("display","inline");

$("#left-side-toggle-close").css("display","none");

}
});

 });




