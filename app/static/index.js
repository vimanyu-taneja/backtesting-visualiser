$(document).on("submit", "#params-form", function (event) {
  event.preventDefault();
  $.ajax({
    type: "POST",
    url: "/",
    data: {
      ticker: $("#ticker").val(),
    },
    success: function (response) {
      $("#plot-container").html(response);
    },
  });
});
