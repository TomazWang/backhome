// static/scripts/decide.js

$(document).ready(function(){

	$('a#btn_yes').click(function(){
		passData(true)
	});

	$('a#btn_no').click(function(){
		passData(false)
	});

	function passData(data){
		$.ajax({
			url:"ajax/decision",
			type:'get',
			data : {
				decision:data	
			},
			success:function(data){
				window.location.replace("see_all")
			}


		});
	}

});