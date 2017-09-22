$(function(){
	$('#group_form').on('submit', function(e){
		e.preventDefault();
		$.ajax({
			url: '/new_group/',
			method: 'post',
			cache: false,
			data: $('#group_form').serialize(),
			success: function(data){
				document.getElementById('groups').innerHTML += data;
			},
			error: function(err){
				console.log(err);
			}
		});
	});

	/*$('.card_form').on('submit', function(e){
		e.preventDefault();
		$.ajax({
			url: '/new_card/',
			method: 'post',
			cache: false,
			data: $('.card_form').serialize(),
			success: function(data){
				console.log(data);
			},
			error: function(err){
				console.log(err);
			}
		});
	});*/
});