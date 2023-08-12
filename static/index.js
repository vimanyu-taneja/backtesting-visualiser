function updateBacktestResults() {
  $.ajax({
    type: "POST",
    url: "/api/generate_plot",
    data: $("#params-form").serialize(),
    success: function (response) {
      $("#plot-container").html(response);
    },
  });
}

$(document).ready(function () {
  updateBacktestResults();
});

$(document).on("submit", "#params-form", function (event) {
  $("#plot-container").html("<div class='loading'></div>");
  event.preventDefault();
  updateBacktestResults();
});
