$('.note-pages button').click(function() {
    $(this).addClass('active').siblings().removeClass('active');
});


// window.onload = function initPDF() {
//     var b = document.getElementsByClassName('card-body');
//     var o = document.getElementById('note-pdf');
//     o.clientHeight = b.height;
// }