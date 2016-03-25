$(document).ready(function () {


	function deselect(e) {
		$('.pop').slideFadeToggle(function () {
			e.removeClass('selected');
		});
	}

	$(function () {
		$(".lastName").on('click', function () {
			if ($(this).hasClass('selected')) {
				deselect($(this));
			} else {
				$(this).addClass('selected');
				$('.pop').slideFadeToggle();
			}
			return false;
		});

		$('.close').on('click', function () {
			deselect($(this));
			return false;
		});
	});

	$.fn.slideFadeToggle = function (easing, callback) {
		return this.animate({
			opacity: 'toggle',
			height: 'toggle'
		}, 'fast', easing, callback);
	};
	
	
	$(".lastName").click(function(){
	lastname_notes($(this))
	});
	
	function lastname_notes(lastname, familynotes){
		var lastname = $.trim(lastname.text());
		var familynotes = $.trim(familynotes.text());
		console.log(familynotes);
		document.getElementById("lastName").innerHTML = lastname;
		document.getElementById("family_notes").innerHTML = lastname;
	}

});