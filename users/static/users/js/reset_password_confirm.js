    $(document).ready(function(){
$("#left-side-toggle-open").css("display","none");
if ($('#complete-checker').val()){

$('#main-form').css('display','none');
$('.description .message').html($('#complete-checker').val());
$('.description').fadeToggle();

}
});