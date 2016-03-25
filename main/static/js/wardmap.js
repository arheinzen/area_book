var map;

function initMap() {
	map = new google.maps.Map(document.getElementById('map'), {
		center: {
			lat: 40.299453,
			lng: -111.713761
		},
		zoom: 16
	});
}