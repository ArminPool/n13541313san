$(document).ready(function(){

$("#left-side-toggle-open").css("display","none");
$("footer").remove();

if ($('#done-checker').val()){

$('#main-form').css('display','none');
$('.description').fadeToggle();
$('.description span').html($('#done-checker').val());
}

$('#show_password_form').click(function(event){


showResetEmail();

});

$('#arrow-back').click(function(event){

ShowLogin();

});


function ShowLogin(){
$('.reset_password_form').css("display","none");
$('#reset-password-header-text').css("display","none");
$('.login_form').fadeToggle();
$('#login-header-text').fadeToggle();

}

function showResetEmail(){

$('.error-fields').css("display","none");

$('.login_form').css("display","none");
$('#login-header-text').css("display","none");
$('.reset_password_form').fadeToggle();
$('#reset-password-header-text').fadeToggle();

}
});