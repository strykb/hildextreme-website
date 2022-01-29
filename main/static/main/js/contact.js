const contactSection = document.getElementById("contact")
const footerHeight = document.querySelector("footer").offsetHeight
contactSection.style.marginTop = navHeight + "px";
contactSection.style.minHeight = window.innerHeight - navHeight - footerHeight + "px";