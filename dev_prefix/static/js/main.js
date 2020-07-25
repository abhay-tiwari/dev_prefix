$(document).ready(function() {

    $('.post-carousel').slick({
        nextArrow: "<div class='slide-prev'><i class='fa fa-angle-left'></i></div>",
        prevArrow: "<div class='slide-next'><i class='fa fa-angle-right'></i></div>",
        infinite: true
    });

    setTimeout(function() {
        $("#alert-message").fadeOut('slow');
    }, 3000);
});