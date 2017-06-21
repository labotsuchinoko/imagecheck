$(document).ready(function() {
$('body').fadeIn(2000);
});

$(function() {
$("#grid").gridalicious({
    width: 100
  });
});

$(document).ready(function() {
    $('a[href="' + this.location.pathname + '"]').parent('li,ul').addClass('active');
});
