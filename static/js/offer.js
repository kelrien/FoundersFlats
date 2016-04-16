var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var labelIndex = 0;
var markerlist = {};

function initMap() {

  // Create a map object and specify the DOM element for display.
  var map = new google.maps.Map(document.getElementById("googleMap"), {
    center:new google.maps.LatLng(49.487760, 8.466242),
    zoom:14,
  });

  addMarker({lat: 49.487760, lng: 8.466242}, map);
  addMarker({lat: 49.489015, lng: 8.472250}, map);
}

// Adds a marker to the map.
function addMarker(location, map) {
  // Add the marker at the clicked location, and add the next-available label
  // from the array of alphabetical characters.
  var l = labels[labelIndex++ % labels.length];
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
