$('.note-pages button').click(function() {
    $(this).addClass('active').siblings().removeClass('active');
});

$(function () {
    $('[data-toggle="popover"]').popover({
        html : true,
        content: function() {
          var content = $(this).attr("data-popover-content");
          return $(content).html();
        }
    })
  })
$('.popover-dismiss').popover({
    trigger: 'focus'
  })