$(document).on("submit", "#params-form", function (event) {
  event.preventDefault();
  $.ajax({
    type: "POST",
    url: "/api/generate_plot",
    data: {
      ticker: $("#ticker").val(),
    },
    success: function (response) {
      $("#plot-container").html(response);
    },
  });
});
