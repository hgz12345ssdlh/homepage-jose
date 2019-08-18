var button = document.getElementsByClassName("topmenu-nav")[0];
var list = document.getElementsByClassName("nav-toggle")[0];
var content = document.getElementsByClassName("content-main")[0];

button.onclick = function() {
  this.classList.toggle("active");
  if (list.style.maxHeight) {
    list.style.maxHeight = null;
    list.style.zIndex = -2;
    content.style.top = "110px";
  } else {
    list.style.maxHeight = list.scrollHeight + "px";
    list.style.zIndex = 0;
    content.style.top = (parseInt(list.scrollHeight) + 110).toString() + "px";
  } 
}
