$(document).ready(function() {


$('#rt-signup').click(function(){
  var email = $('#email').val();
  var name = $('#name').val();
  var newSignup = $.ajax({
    data: {test: email},
    type: 'post',
    url: '/recordtrac',
    contentType: 'application/json;charset=UTF-8',
  })
  newSignup.done(function( msg ) {
    console.log(newSignup)
    alert(newSignup)
  });
})

});
