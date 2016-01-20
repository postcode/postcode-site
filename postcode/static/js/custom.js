$(document).ready(function() {
  $( "#email" ).keypress(function( event ) {
    $('.areyouhuman').show()
  })
  if($('.recaptcha-error').text().length > 0) {
    $('.areyouhuman').show()
  }
  $('#message-modal').modal('show')
});
