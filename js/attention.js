var attention = document.getElementsByClassName("course-attention")[0];
var words = document.getElementsByClassName("attention-toggle")[0];

attention.onclick = function() {
  if (!words.style.display || words.style.display == "none") {
    words.style.display = "block";
  } else {
    words.style.display = "none";
  }
}
