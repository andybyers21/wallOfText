function textJoin() {
  let text1 = $('#text1').val();
  let text2 = $('#text2').val();
  $.ajax({
    url: '/join',
    type: 'POST',
    data: { text1: text1, text2: text2 },
  }).done(function (response) {
    let html = '<br><br><br><p> <b> RESULT : <b><p>';

    response = response.result;
    $.each(response, function (key, val) {
      console.log(val);
      html += '<p>' + val + '<p>';
    });

    html += '<br>';
    $('.show-data').append(html);
  });
}
