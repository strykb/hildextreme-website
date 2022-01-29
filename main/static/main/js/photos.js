const photosSection = document.getElementById("photos")
const footerHeight = document.querySelector("footer").offsetHeight
photosSection.style.marginTop = navHeight + "px";
photosSection.style.minHeight = window.innerHeight - navHeight - footerHeight + "px";