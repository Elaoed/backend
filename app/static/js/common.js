$(function(){
    $(".nav a").on("click", function(){
        $(this).parent().parent().find("a").removeClass('active-menu');
        $(this).addClass("active-menu");
    });
});