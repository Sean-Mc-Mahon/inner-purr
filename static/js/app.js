//MATERIALIZE FUNCTIONS
$(document).ready(function () {
  $('.sidenav').sidenav({edge: "right",inDuration: 1000});
  $('.parallax').parallax();
  $('.dropdown-trigger').dropdown();
  $("#carousel-small").carousel();
  $('.slider').slider({
    interval: 10000,
  });
  $("#carousel-full").carousel({
    fullWidth: true,
    indicators: true,
  });
  $(document).ready(function(){
    $('select').formSelect();
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


//FOCUS DROPDOWN MENU
function show() {
    const arrow = document.querySelector('#dropdown-arrow')
    const dropped = document.querySelector('.profile-dropped')
    dropped.classList.toggle('show')
    arrow.classList.toggle('rotated')
}

document.addEventListener('click', function(e) {
    const arrow = document.querySelector('#dropdown-arrow')
    const dropped = document.querySelector('.profile-dropped')
    if (e.target.closest('.profile-drop')) return
    dropped.classList.remove('show')
    arrow.classList.remove('rotated')
})