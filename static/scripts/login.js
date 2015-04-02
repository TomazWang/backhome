// scripts/login.js

$(document).ready(function (){

	$('#btn_login').click(function(){

		$('a#btn_login').hide();
		$('.lead').hide();
		$('#login_form').show();
	});

	$('#login_link').click(function(){
		
		function loginFail(){
			alert("登入錯誤");
		}

		if(($('#input_name').val() != "")&&($('#input_pass').val() != "")){ 

			$.ajax({
				url:'ajax/login',
				typr:'GET',
				data:{
					member_name:$('#input_name').val(),
					key : $('#input_pass').val()
				},
				dataType:'json',
				success:function(data){
					status = data[0]['status'];
					if(status == 'success'){
						m_id = data[0]['member_id'];
						m_name = data[0]['member_name'];
						key = data[0]['key'];

						window.location = './?m_id='+m_id+'&key='+key;


					}else if(status == 'key_wrong'){
						alert("密碼錯誤");
					}else{
						loginFail();
					}
				},
				error:function(){
					loginFail();
				}
			});

		}else{
			$("#warning-text").append("請輸入名字與密碼");
		}
	});

	var handler = function(){
		search_member();
	};

	$('#input_name').focus(function(){
		$(document).bind('keyup',handler);

	});

	$('#input_name').focusout(function(){
		$(document).unbind('keyup',handler);
	});

	// $('#input_name').change(function(){
	// 	search_member();
	// });


	function resultItemClick(){
		$('.result_item').click(function(){
			result_item = $(this);

			$('#input_name').val(result_item.text());
			$('#search_result_block').hide();
		});

	}

	function search_member(){
		member_name = $('#input_name').val().trim();

		if(member_name != '' && member_name != undefined){

			$('#search_result_block').show();
			search_result = $('#search_result');

			$.ajax({
				url:'ajax/search_member',
				typr:'GET',
				data:{
					member_name:member_name
				},
				dataType:'json',
				success:function(Jdata){
					search_result.empty();

					for(var i=0; i<Jdata.length;i++){
						html = '<a class="result_item list-group-item"';
						html += 'value="'
						html += Jdata[i]['id'];
						html += '">';
						html += Jdata[i]['name'];
						html += '</a>'
						search_result.append(html);
					}

					html = "<a id='cant_find_me' class='list-group-item'>找不到我</a>";
					search_result.append(html);
					resultItemClick();
				},

				error:function(){
					alert("Something's worng.");
				}
			});

		}else{
			$('#search_result_block').hide();
		}
	}


});