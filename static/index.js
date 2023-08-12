$(document).on("submit", "#params-form", function (event) {
  event.preventDefault();
  $.ajax({
    type: "POST",
    url: "/api/generate_plot",
    data: $("#params-form").serialize(),
    success: function (response) {
      $("#plot-container").html(response);
    },
  });
});
