// this changes the navbar color from transparent to dark
document.addEventListener("scroll", function (){
    if (window.scrollY < 100 ) {
        nav.classList.remove("bg-dark");
    } 
    else {
        nav.classList.add("bg-dark");
    }
});