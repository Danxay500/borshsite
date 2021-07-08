'use strict'; //современный режим

window.onload = function() {

    const mobileMenuButton = document.querySelector(".mobile-menu-button");
    const mobileMenu = document.querySelector(".mobile-menu");
    const mobileMenuButtonLine = document.querySelectorAll(".mobile-menu-button-line");

    let openOrClose = false;

    mobileMenuButton.addEventListener("click", ()=>{
        if (openOrClose == false) {
            mobileMenu.style.display = "block";
            setTimeout(()=>{
                mobileMenu.style.transform = "translateY(0)"
            }, 0)
            for (let i = 0; i < mobileMenuButtonLine.length; i++) {
                mobileMenuButtonLine[i].style.background = "#ffffff";
            }
            openOrClose = true;
        }
        else {
            setTimeout(()=>{
                mobileMenu.style.display = "none";
            }, 300)
            for (let i = 0; i < mobileMenuButtonLine.length; i++) {
                mobileMenuButtonLine[i].style.background = "#000000";
            }
            mobileMenu.style.transform = "translateY(-220px)"
            openOrClose = false;
        }
    })

}