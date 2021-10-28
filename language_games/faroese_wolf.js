$(document).ready(function() {
  $("#image-div").addClass("hidden");
});

var image = document.getElementById("test-image")

function begin(){
  $("#start_button").hide();
  $("#instructions-1").text("Please name this animal in Faroese:").addClass("big-instructions");
  $("#image-div").removeClass("hidden");
};
