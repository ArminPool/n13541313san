$(document).ready(function() {

           /*        form validation            */
   $("#SideForm").validate({


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
$('.uo-nested-dropdown a').on("click", function(e){
 $(this).next('ul').toggle();
 e.stopPropagation();
 });
 $('.poc-nested-dropdown a').on("click", function(e){
 $(this).next('ul').toggle();
 e.stopPropagation();
 });


var pageURL = $(location).attr("href");

$('body').css('padding-top',$('.navbar-fixed-top').css("height"));




// or just with selector string

    $(function(){
        $('input').blur();
    });
var pageURL = $(location).attr("href");



var sideNav;
var headerWidth = parseFloat($(".navbar-header").css("width")) ;
var ScreenWidth = $(window).width();
var ScreenHeight = $(window).height();
if(ScreenHeight < 477){


$('#SideNav').css('position','relative');
$('#SideNav').css('top','0px');


}

if(ScreenWidth < 752){
$(".navbar-default .navbar-nav > li > a").attr("data-toggle","dropdown");

$(".navbar-collapse").css("margin-right","0px");
$(".navbar-collapse").css("border-top","2px solid #fff");

$(".navbar-right").css("padding-right","0px");


}
if (ScreenWidth > 951){

$('#navbar1 .container-fluid').css('padding-left','46px')
$('#navbar1 .container-fluid').css('padding-right','46px')

}


/*
if( headerWidth > 97){


$(".navbar-header").css("padding-right","50px");
$(".navbar-brand").css("padding-left","0px");
}
else{
$(".navbar-brand").css("padding-left","15px");
$(".navbar-header").css("padding-right","0px");
}
if( pageURL == "http://arminoldboy.pythonanywhere.com/"){
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
*/
$("#left-side-toggle-open").click(openNav);
$("#left-side-toggle-close").click(closeNav);



$(window).on('resize', function(){
$('.menu5').removeAttr("style");
$('.menu6').removeAttr("style");


$('body').css('padding-top',"" + $('.navbar-fixed-top').css("height"));

if($(this).height() != ScreenHeight){

if($(this).height() > 477){


$('#SideNav').css('position','fixed');
$('#SideNav').css('top',$('.navbar-fixed-top').css("height"));


}
/*
else if ($(this).height() < 477 && $(this).width() < 586 ){
$('#SideNav').css('position','relative');
$('#SideNav').css('top','134px');
console.log("2");
}
*/
else{

$('#SideNav').css('position','relative');
$('#SideNav').css('top','0px');
}

ScreenHeight= $(this).height();
}
else if ($(this).height() == ScreenHeight && $(this).width() > 586 ){

$('#SideNav').css('position','relative');
$('#SideNav').css('top','0px');

}

if($(this).width() != ScreenWidth){

if($(this).width() < 951){

$('#navbar1 .container-fluid').css('padding-left','15px')
$('#navbar1 .container-fluid').css('padding-right','15px')

}
else{
$('#navbar1 .container-fluid').css('padding-left','46px')
$('#navbar1 .container-fluid').css('padding-right','46px')

}
if($(this).width() < 752){
$(".navbar-default .navbar-nav > li > a").attr("data-toggle","dropdown");
$(".navbar-collapse").css("margin-right","0px");
$("p.navbar-right").css("padding-right","0px");
$(".navbar-collapse").css("border-top","2px solid #fff");




}
else{
$(".navbar-collapse").css("margin-right","253px");

$(".navbar-default .navbar-nav > li > a").attr("data-toggle","");
$("p.navbar-right").css("padding-right","15px");
$(".navbar-collapse").css("border-top","none");

if($(".education-dropdown.open").length > 0){

$(".open[role=presentation]").removeClass().addClass("dropdown").addClass("education-dropdown");

}

if($(".poc-nested-dropdown.open").length > 0){

$(".open[role=presentation]").removeClass().addClass("dropdown").addClass("poc-nested-dropdown");

}
if($(".article-dropdown.open").length > 0){

$(".open[role=presentation]").removeClass().addClass("dropdown").addClass("article-dropdown");

}
if($(".money-dropdown.open").length > 0){

$(".open[role=presentation]").removeClass().addClass("dropdown").addClass("money-dropdown");


}
if($(".trading-accounts-dropdown.open").length > 0){

$(".open[role=presentation]").removeClass().addClass("dropdown").addClass("trading-accounts-dropdown");

}


}


var headerWidth = parseFloat($(".navbar-header").css("width")) ;
var headerPadding = parseFloat($(".navbar-header").css("padding-right")) ;

/*
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
*/

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
RemoveOrShowFooter();

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
$("#SideNav").css("position","relative");
$("#SideNav").css("top","0px");


$("#left-side-toggle-open").css("display","none");

$("#left-side-toggle-close").css("display","inline");

}
else{
$("#main").css("display","block");
RemoveOrShowFooter();

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


RemoveOrShowFooter();

$("#main").css("display","block");



$("#SideNav").css("width","0px");
$("#left-side-toggle-open").css("display","inline");

$("#left-side-toggle-close").css("display","none");

}
else{
RemoveOrShowFooter();

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
var Poc_dropdown;
var Uo_dropdown;

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

$(".navbar-default .navbar-nav .poc-nested-dropdown  a").click(function(event){


if( Poc_dropdown == 1 ){

$(".menu5").css("display","none");


Poc_dropdown=2;

}

else{

$(".menu1").css("display","none");

$(".menu2").css("display","none");

$(".menu3").css("display","none");

$(".menu4").css("display","none");

$(".menu5").css("display","block");




Article_dropdown =2;

Money_dropdown =2;

Poc_dropdown = 1;
}

});

}
}

function RemoveOrShowFooter(){
if( pageURL == "https://navasangold.com/" || pageURL == "http://navasangold.com/"
 || pageURL == "https://www.navasangold.com/" || pageURL == "http://www.navasangold.com/" ){

$("footer").css("display","none");


}
else{
$("footer").css("display","block");
}

}

 });




