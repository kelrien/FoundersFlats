var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var markerlist = {};


function initMap() {

  // Create a map object and specify the DOM element for display.
  var map = new google.maps.Map(document.getElementById("googleMap"), {
    center:new google.maps.LatLng(49.487760, 8.466242),
    zoom:14,
  });
  var geocoder = new google.maps.Geocoder();
  $(todo_markers).each(function(index, val) {geocodeAddress(geocoder, map, index, val);});
}

// Adds a marker to the map.
function addMarker(location, map, id) {
  // Add the marker at the clicked location, and add the next-available label
  // from the array of alphabetical characters.
  var l = labels[id];
  var marker = new google.maps.Marker({
    position: location,
    label: l,
    map: map,
    icon: normalIcon()
  });
  markerlist[l] = marker;

  marker.addListener('click', function() {
    scrollToEntry(marker.getLabel());
  });
}

function geocodeAddress(geocoder, map, index, address) {
  geocoder.geocode({'address': address}, function(results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
      addMarker(results[0].geometry.location, map, index);
    } else {
      addMarker({lat: 49.487760, lng: 8.466242}, map, index);
    }
  });
}

function scrollToEntry(id) {
  $("#entrylist").animate({scrollTop: $("#entry-"+id).offset().top-$("#entrylist").offset().top}, 'fast');
  $("#entry-"+id).css("backgroundColor", "#eee");
  $("#entry-"+id).animate({backgroundColor: "#fff"}, 700 );
}

$("#entrylist .entry").hover(
  function() {
        markerlist[$(this)[0].id.replace("entry-", "")].setIcon(highlightedIcon());
  }, function() {
        markerlist[$(this)[0].id.replace("entry-", "")].setIcon(normalIcon());
  }
);

function toggleBounce(marker, start) {
  if (start) {
    marker.setAnimation(google.maps.Animation.BOUNCE);
  } else {
    marker.setAnimation(null);
  }
}
// functions that return icons.  Make or find your own markers.
function normalIcon() {
  return {
    url: 'static/media/marker.png'
  };
}
function highlightedIcon() {
  return {
    url: 'static/media/marker-active.png'
  };
}


$(function () {
  var a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  $( ".entry" ).each(function( index ) {$(this).attr("id", "entry-"+a[index]); $(this).find(".number").text(a[index])});
})