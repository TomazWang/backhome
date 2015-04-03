// static/scripts/decide.js

$(document).ready(function(){

	$('a#btn_yes').click(function(){
		passData(1);
	});

	$('a#btn_no').click(function(){
		passData(0);
	});

	$('a#btn_change_to_yes').click(function(){
		passData(1);
	});


	$('a#btn_change_to_no').click(function(){
		passData(0);
	});

	$('a#btn_change').click(function(){
		$('a#btn_change').hide();
		$('#change_decision_block').show();
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