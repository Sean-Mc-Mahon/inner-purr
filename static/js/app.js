//MATERIALIZE FUNCTIONS
$(document).ready(function () {
  $('.sidenav').sidenav({edge: "right",inDuration: 1000});
  $('.parallax').parallax();
  $("#carousel-small").carousel();
  $('.slider').slider({
    interval: 10000,
  });
  $("#carousel-full").carousel({
    fullWidth: true,
    indicators: true,
  });
});

//CAT SVG CHASES MOUSE
//Code modified from: https://daily-dev-tips.com/posts/javascript-mouse-tracking-eyes-%F0%9F%91%80/
document.addEventListener("mousemove", (e) => {
  const eyes = document.querySelectorAll(".stitches");
  const paws = document.querySelectorAll(".paws");
  [].forEach.call(eyes, function (eye) {
    // Get the mouse position on the horizontal axis
    let mouseX = eye.getBoundingClientRect().right;
    if (eye.classList.contains("eye-left")) {
      mouseX = eye.getBoundingClientRect().left;
    }
    // Get the vertical offset
    let mouseY = eye.getBoundingClientRect().top;
    // Calculate the radian value of the offset between the mouse and the eye
    let radianDegrees = Math.atan2(e.pageX - mouseX, e.pageY - mouseY);
    // Convert into a degree based value to use in CSS
    let rotationDegrees = radianDegrees * (180 / Math.PI) * -1 + 180;
    // Add this degrees to the eye
    eye.style.transform = `rotate(${rotationDegrees}deg)`;
  });
  [].forEach.call(paws, function (paw) {
    let mouseY = eye.getBoundingClientRect().bottom;
    // Calculate the radian value of the offset between the mouse and the paw
    let radianDegrees = Math.atan2(e.pageX - mouseX, e.pageY - mouseY);
    // Convert into a degree based value to use in CSS
    let rotationDegrees = radianDegrees * (90 / Math.PI) * -1 + 90;
    // Add this degrees to the paw
    eye.style.transform = `rotate(${rotationDegrees}deg)`;
  });
});


//SCROLL EFFECTS
function scrollAppear() {
  const menuText = document.querySelector(".menu-text");
  const menuPosition = menuText.getBoundingClientRect().top;
  const catText = document.querySelector(".cat-text");
  const catPosition = catText.getBoundingClientRect().top;
  const catCarousel = document.querySelector("#carousel-small");
  const carouselPosition = catCarousel.getBoundingClientRect().top;
  var screenPosition = window.innerHeight / 1.3;
  if (menuPosition < screenPosition) {
    menuText.classList.add("text-appear");
  }
  if (catPosition < screenPosition) {
    catText.classList.add("text-appear");
  }
  if (carouselPosition < screenPosition) {
    catCarousel.classList.add("text-appear");
  }
}


window.addEventListener("scroll", scrollAppear);
