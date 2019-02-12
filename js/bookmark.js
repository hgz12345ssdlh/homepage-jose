var trigger = document.getElementsByClassName("trigger")[0];
var bookmark = document.getElementsByClassName("bookmark")[0];

trigger.onclick = function() {
  this.classList.toggle("active");
  if (bookmark.style.right == "0px") {
    bookmark.style.right = "-500px";
    this.style.right = "-90px";
  } else {
    bookmark.style.right = "0px";
    this.style.right = "410px";
  } 
}
