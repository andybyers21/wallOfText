// Text join test
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


// Text Editor
document.getElementById("heading").innerHTML =
  localStorage["title"] || "Just Write"; // default text
document.getElementById("content").innerHTML =
  localStorage["text"] || "This text is automatically saved every second :) "; // default text

setInterval(function() {
  // fuction that is saving the innerHTML of the div
  localStorage["title"] = document.getElementById("heading").innerHTML; // heading div
  localStorage["text"] = document.getElementById("content").innerHTML; // content div
}, 1000);


// TODO: Print text to new page
function printText() {
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


