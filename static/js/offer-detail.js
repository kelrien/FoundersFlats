function initMap() {

  // Create a map object and specify the DOM element for display.
  var map = new google.maps.Map(document.getElementById("googleMap"), {
    center:new google.maps.LatLng(49.487760, 8.466242),
    zoom:14,
  });
  var geocoder = new google.maps.Geocoder();

  geocodeAddress(geocoder, map, _address);
}

// Adds a marker to the map.
function addMarker(location, map) {
  // Add the marker at the clicked location, and add the next-available label
  // from the array of alphabetical characters.
  var marker = new google.maps.Marker({
    position: location,
    map: map
  });
}

function geocodeAddress(geocoder, map, address) {
  geocoder.geocode({'address': address}, function(results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
      addMarker(results[0].geometry.location, map);
      map.setCenter(results[0].geometry.location);
    } else {
      addMarker({lat: 49.487760, lng: 8.466242}, map);
      map.setCenter({lat: 49.487760, lng: 8.466242});
    }
  });
}

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})