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
				document.getElementById('group_form').reset();
			},
			error: function(err){
				console.log(err);
			}
		});
	});
});