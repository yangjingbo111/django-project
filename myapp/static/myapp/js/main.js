// <script src="{% static 'myapp/js/jquery.js' %}"></script>


$( document ).ready(function(){
	$('h1').html('changed');
});

$('#btn1').click(function(){
	console.log('btn1 click');
});

$('#img1').click(function(){
	console.log('image is clicked');
	$('#img1').css('height', 400)
});
// $("h1").html("<p>changed</p>")
// alert('this is an alert')
