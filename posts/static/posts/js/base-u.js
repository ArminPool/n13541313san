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
 var st;
var isScrolling;
var didScroll;
var lastScrollTop = 0;
var navbar_added_new = false;
var delta = 5;
var distance_to_first=0;
var navbarHeight = $('#navbar-container').outerHeight();
$(window).scroll(function(event){
    console.log('window is on scroll');

    window.clearTimeout( isScrolling );

    didScroll = true;
    st = $(this).scrollTop();

    updatevariables();
    isScrolling = setTimeout(function() {


        // Run the callback
        hasScrolled();
        $('#navbar-collapse').removeClass('in');

        if ( distance_to_first < 10 ){

            $('.navbar-fixed-top').css('transform','');

           //$('#navbar-container').addClass('navbar-fixed-top');

        }
 if($('.navbar-fixed-top').length > 0 && distance_to_first > 0) {
     $("#main").css("margin-top",navbarHeight);

        }
        else if($('.navbar-fixed-top').length > 0 && distance_to_first == 0) {

            $("#main").css("margin-top",navbarHeight);



        }

    }, 100);
});


function updatevariables() {


    // Make sure they scroll more than delta
    if(Math.abs(lastScrollTop - st) <= delta)
        return;

        if(st < lastScrollTop){
                distance_to_first = distance_to_first - Math.abs(lastScrollTop - st);




        }
        else if (st > lastScrollTop){
                        distance_to_first = distance_to_first + Math.abs(lastScrollTop - st);



        }


        lastScrollTop = st;
}


function hasScrolled() {


    // If they scrolled down and are past the navbar, add class .nav-up.
    // This is necessary so you never see what is "behind" the navbar.
    if (st < lastScrollTop && $(window).width() < 586 && sideNav == 1 ){
    }
    else if(st < lastScrollTop){
        // Scroll up


// $('#navbar-container').addClass('navbar-fixed-top');
$('.navbar-fixed-top').css('transform','');


 if(sideNav == 1) {
 $('#SideNav').css('width','250px');
             $('#main').css('margin-right','250px')

    } else {
    if ( $(window).width() < 586 && sideNav == 1 ){

    }
    }
    }
    else if(st > lastScrollTop){


        // Scroll Down
        if(st + $(window).height() < $(document).height() && sideNav != 1) {
        $("#main").css("margin-top",'0px');

         $('#SideNav').css('width','0px');
         $('#main').css('margin-right','0px');
         $('.navbar-fixed-top').css('transform','translateY(-100%)');


 //$('#navbar-container').removeClass('navbar-fixed-top');


}

        }



    }



var uo_nested_dropdown ;
var poc_nested_dropdown ;
$('.uo-nested-dropdown a').on("click", function(e){
if ($(window).width() < 745){
  if (uo_nested_dropdown == 1){
   $(this).parent('li').first().removeClass('open');
   uo_nested_dropdown = 2;
$('menu5').css('display','none');
   $(this).css('background-color','transparent');
         $(this).css('color','#fff');


  }
  else{
   $(this).parent('li').first().addClass('open');

uo_nested_dropdown = 1;
   $(this).css('background-color','#e7e7e7');
      $(this).css('color','#555');

$('menu5').css('display','block');
  }

 e.stopPropagation();
 }
 });
$('.poc-nested-dropdown a').on("click", function(e){
if ($(window).width() < 745){
  if (poc_nested_dropdown == 1){
   $(this).parent('li').first().removeClass('open');
      $(this).css('background-color','transparent');

$('menu6').css('display','none');
      $(this).css('color','#fff');

poc_nested_dropdown = 2;
  }
  else{
   $(this).parent('li').first().addClass('open');
poc_nested_dropdown = 1;
   $(this).css('background-color','#e7e7e7');
      $(this).css('color','#555');


$('menu6').css('display','block');
  }

 e.stopPropagation();
 }
 });

var pageURL = $(location).attr("href");





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
$('#SideNav').css('margin-top',navbarHeight);


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

navbarHeight = $('#navbar-container').outerHeight();
$('.uo-nested-dropdown a').removeAttr("style");
$('.poc-nested-dropdown a').removeAttr("style");

$('.menu5').removeAttr("style");
$('.menu6').removeAttr("style");




if($(this).width() != ScreenWidth){
    navbarHeight = $('#navbar-container').outerHeight();
    console.log(navbarHeight);

  

$("#main").css("margin-top",navbarHeight);


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

$("li.education-dropdown").removeClass('open');

}

if($(".poc-nested-dropdown.open").length > 0){

$("li.poc-nested-dropdown").removeClass('open');

}
if($(".uo-nested-dropdown.open").length > 0){

$("li.uo-nested-dropdown").removeClass('open');
}
if($(".article-dropdown.open").length > 0){

$("li.article-dropdown").removeClass('open');

}
if($(".money-dropdown.open").length > 0){

$("li.money-dropdown").removeClass('open');


}
if($(".trading-accounts-dropdown.open").length > 0){

$("li.trading-accounts-dropdown").removeClass('open');

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
$("#SideNav").css("margin-top","0px");


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
$("#SideNav").css("margin-top",navbarHeight);


$("#left-side-toggle-open").css("display","none");

$("#left-side-toggle-close").css("display","inline");

}
else{
$("#main").css("display","block");
RemoveOrShowFooter();

$("#SideNav").css("margin-top","0px");

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




