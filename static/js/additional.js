// adds height of navbar to scrolling using anchors
const nav = document.getElementById('main-navbar');
const navHeight = nav.offsetHeight;
document.querySelector("html").style.scrollPaddingTop = navHeight + "px";