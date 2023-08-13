$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (
      !/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) &&
      !this.crossDomain
    ) {
      xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}");
    }
  },
});

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

$("#params-form").submit(function (e) {
  $("#plot-container").html("<div class='loading'></div>");
  e.preventDefault();
  updateBacktestResults();
});
