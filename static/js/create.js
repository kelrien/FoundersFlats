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


});