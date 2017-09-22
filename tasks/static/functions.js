function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function createCard(group_id){
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});
	$.ajax({
		url: '/new_card/',
		method: 'post',
		cache: false,
		data: $('#card_form_' + group_id).serialize(),
		success: function(data){
			var resp_obj = JSON.parse(data);
			var group_id = resp_obj.group_id;
			var html = resp_obj.html;
			document.getElementById('cards-for-' + group_id).innerHTML += html;
			document.getElementById('card_form_' + group_id).reset();
		},
		error: function(err){
			console.log(err);
		}
	});
}

function deleteCard(id){
	$.ajax({
		url: '/del_card/',
		method: 'post',
		cache: false,
		data: { card_id: id },
		success: function(data){
			var card_id = data;
			card = document.getElementById('card_' + card_id);
			card.parentNode.removeChild(card);
		},
		error: function(err){
			console.log(err);
		}
	});
}

function checkCard(id){
	$.ajax({
		url: '/check_card/',
		method: 'post',
		cache: false,
		data: { card_id: id },
		success: function(data){
			var card_id = data;
			document.getElementById('card_check_' + card_id).classList.add('visible');
		},
		error: function(err){
			console.log(err);
		}
	});
}

function delGroup(id){
	$.ajax({
		url: '/del_group/',
		method: 'post',
		cache: false,
		data: { group_id: id },
		success: function(data){
			var group_id = data;
			group = document.getElementById('group_' + group_id);
			group.parentNode.removeChild(group);
		},
		error: function(err){
			console.log(err);
		}
	});
}