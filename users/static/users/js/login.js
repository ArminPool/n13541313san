$(document).ready(function(){
$(this).scrollTop(0);
$("#left-side-toggle-open").css("display","none");
$("footer").remove();

if ($('#message-checker').val()){

$('#main-form').css('display','none');
$('.description').fadeToggle();
$('.description .message').html($('#message-checker').val());
}
$('#show_password_form').click(function(event){


showResetEmail();

});
$('#arrow-back-from-email-form').click(function(event){

ShowLoginFromEmailForm();

});
$('#arrow-back-from-message-div').click(function(event){

ShowLoginFromMessageDiv();

});


function ShowLoginFromEmailForm(){
$('.reset_password_form').css("display","none");
$('#reset-password-header-text').css("display","none");
$('.login_form').fadeToggle();
$('#login-header-text').fadeToggle();

}
function ShowLoginFromMessageDiv(){
$('#main-form').fadeToggle();
$('.description').css('display','none');

$('.reset_password_form').css("display","none");
$('#reset-password-header-text').css("display","none");

}

function showResetEmail(){

$('.error-fields').css("display","none");

$('.login_form').css("display","none");
$('#login-header-text').css("display","none");
$('.reset_password_form').fadeToggle();
$('#reset-password-header-text').fadeToggle();

}

});
