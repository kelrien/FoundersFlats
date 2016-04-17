$(function () {
	$(".datepicker").datepicker({
		format: "dd.mm.yyyy",
		autoclose: true
	});
	$('[data-toggle="tooltip"]').tooltip();

	$(".ff-checkbox-toggle").click(function() {
		var state = $(this).find("input").val();
		if(state == "0") {
			$(this).find(".state").text("✔");
			$(this).find("input").val(1);
		} else {
			$(this).find(".state").text("✘");
			$(this).find("input").val(0);
		}
	});

	$('form').validator();

});


// This example adds a search box to a map, using the Google Place Autocomplete
// feature. People can enter geographical searches. The search box will return a
// pick list containing a mix of places and predicted search terms.

function initAutocomplete() {
  var map = new google.maps.Map(document.getElementById('map'));

  // Create the search box and link it to the UI element.
  var input = document.getElementById('pac-input');
  var searchBox = new google.maps.places.SearchBox(input);
}