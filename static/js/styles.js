window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop >180 || document.documentElement.scrollTop > 180) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-80px";
  }
}
