// Text Editor
document.getElementById("heading").innerHTML =
  localStorage["title"] || "Wall of Text"; // default text
document.getElementById("content").innerHTML =
  localStorage["text"] || "Delete this text and type of paste your text to be formatted into this box."; // default text

setInterval(function() {
  // fuction that is saving the innerHTML of the div
  localStorage["title"] = document.getElementById("heading").innerHTML; // heading div
  localStorage["text"] = document.getElementById("content").innerHTML; // content div
}, 1000);

