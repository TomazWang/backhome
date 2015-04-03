// scripts/signin.js

$(document).ready(function(){

	// get group list
	$.ajax({
		
		url:'ajax/get_all_group',
		type:'GET',
		dataType:'json',
		success:function(data){

			for(var i=0;i<data.length;i++){
				html = '<option value="';
				html += data[i]['gID'];
				html += '">';
				html += data[i]['gName'];
				html += '</option>';
				$("#input_group").append(html);
			}

		},

		error:function(){
		}
	});



	var use_group_selector = true;

	$('#btn_show_add_group').click(function(){
		$('#group_select_block').hide();
		$('#add_group_input_block').show();

		use_group_selector = false;

	});

	$('#btn_show_select_group').click(function(){
		$('#group_select_block').show();
		$('#add_group_input_block').hide();

		use_group_selector = true;
	});


	$('#signin_link').click(function(){

		name = $('#input_name').val();
		key = $('#input_pass').val();
		m_id = 0;
		group_id = 0;

		if(use_group_selector){
			
			group_id = $('#input_group').val();
			
			if(name == ""||key==""){
				alert("請輸入名字與密碼");
				return;
			}

			if(group_id == 0){
				alert("請選擇你隸屬的家庭");
				return;
			}

			$.ajax({

				url:'ajax/new_member',
				type:'GET',
				data:{
					new_member_name:name,
					group_id:group_id,
				},
				dataType:'json',
				success:function(data){
					if(data.length <= 0){ return;}

					status = data[0]['status'];
					if(status == 'success'){
						m_id = data[0]['member_id'];

						window.location = './?m_id='+m_id+'&key='+key;

					}

				},
				error:function(){}
			});


		}else{

		}



	});


});

