$(document).ready(function() {
$(".comments span + button").click(function(event){
    event.preventDefault();
    $(this).nextAll('form').first().fadeToggle();
});

$(".show-replies").click(function(event){
    event.preventDefault();
     $(this).nextAll('.see-replies').first().fadeToggle();
});
 $("textarea").before("<label>پیام</label>");


$('blockquote').filter(function(){return $(this).text().trim().length==0}).remove();

});