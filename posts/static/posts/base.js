$(document).ready(function() {

           /*        form validation            */
   $("#SideForm").validate({

  rules: {
    username: "required",
    password1: {
      required: true,
      password: true
    }
  },
  messages: {
    username: "لطفا اسم خود را وارد کنید ",
    password1:"لطفا رمز عبور خود را وارد کنید ",
  }
  ,
   errorPlacement: function (error, element) {
        error.css({'color':'#fff'});

        error.insertAfter(element);
    }
});




    $(function(){
        $('input').blur();
    });
var pageURL = $(location).attr("href");

if( pageURL == "http://127.0.0.1:8000/user/reset-password/confirm/"){

$("footer").remove();

}

var sideNav;
var headerWidth = parseFloat($(".navbar-header").css("width")) ;
var ScreenWidth = $(window).width();
if(ScreenWidth < 750){
$(".navbar-default .navbar-nav > li > a").attr("data-toggle","dropdown");


}

if( headerWidth > 97){


$(".navbar-header").css("padding-right","50px");
$(".navbar-brand").css("padding-left","0px");
}
else{
$(".navbar-brand").css("padding-left","15px");
$(".navbar-header").css("padding-right","0px");
}
if( pageURL == "http://127.0.0.1:8000/"){
var ScreenWidth = $(window).width();
if(ScreenWidth < 586){

$("#main").css("display","block");
$("#SideNav").css("width","0px");
}
else{
sideNav = 1;
$("#main").css("margin-right","250px");
$("#SideNav").css("width","250px");
$("#left-side-toggle-open").css("display","none");
$("#left-side-toggle-close").css("display","inline");

}
}
$("#left-side-toggle-open").click(openNav);
$("#left-side-toggle-close").click(closeNav);



$(window).on('resize', function(){

if($(this).width() != ScreenWidth){


if($(this).width() < 750){
$(".navbar-default .navbar-nav > li > a").attr("data-toggle","dropdown");


}
else{

$(".navbar-default .navbar-nav > li > a").attr("data-toggle","");


}





var headerWidth = parseFloat($(".navbar-header").css("width")) ;
var headerPadding = parseFloat($(".navbar-header").css("padding-right")) ;
if ($(this).width() > ScreenWidth){

if( (headerWidth - headerPadding) > 97 && (headerPadding > 0) ){

$(".navbar-brand").css("padding-left","0px");
$(".navbar-header").css("padding-right","50px");
}
else{

$(".navbar-brand").css("padding-left","15px");
$(".navbar-header").css("padding-right","0px");
}
}
else{
if((headerWidth - headerPadding) > 97){


$(".navbar-header").css("padding-right","50px");
$(".navbar-brand").css("padding-left","0px");
}
}


if($(this).width() < 586){
if(sideNav == 1){
$("#main").css("marginRight","0px");
$("#SideNav").css("width","0px");
$("#left-side-toggle-open").css("display","none");
$("#main").css("display","block");
$("#left-side-toggle-close").css("display","inline");
}
}

else{
if(sideNav == 1){
$("#main").css("display","block");
$("footer").css("display","block");
$("#main").css("marginRight","250px");
$("#SideNav").css("width","250px");
$("#left-side-toggle-open").css("display","none");

$("#left-side-toggle-close").css("display","inline");
}
}
 ScreenWidth = $(this).width();
}



});


function openNav(){

sideNav = 1;

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
$("#main").css("margin-right","250px");
$("#SideNav").css("width","250px");
$("#left-side-toggle-open").css("display","none");

$("#left-side-toggle-close").css("display","inline");
}

}

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


function dropdown_handler(SWidth){
var Article_dropdown;
var Money_dropdown;

if(SWidth > 750){

$(".navbar-default .navbar-nav > li > a").click(function(event){

$(this).nextAll('.dropdown-menu').first().css("display","none");


});



$(".navbar-default .navbar-nav > li > a").hover(function(event){

$(this).nextAll('.dropdown-menu').first().css("display","block");


});
}
else{


                    /* handling first dropdown */


$(".navbar-default .navbar-nav .article-dropdown  a").click(function(event){


if( Article_dropdown == 1 ){

$(".menu1").css("display","none");


Article_dropdown=2;
}
else{
$(".menu2").css("display","none");

$(".menu1").css("display","block");


Article_dropdown =1;
Money_dropdown =2;

}

});
                      /* handling second dropdown */


$(".navbar-default .navbar-nav .money-dropdown  a").click(function(event){


if( Money_dropdown == 1 ){
$(".menu2").css("display","none");


Money_dropdown=2;
}
else{
$(".menu1").css("display","none");

$(".menu2").css("display","block");

Article_dropdown =2;

Money_dropdown =1;
}

});


}
}

 });




