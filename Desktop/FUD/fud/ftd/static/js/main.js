// show dropdown when user click on Account
let dropdownLinks = document.querySelectorAll(".dropdown-link");
let dropdown = document.querySelector(".dropdown-account");

dropdownLinks.forEach((link) => {
    link.addEventListener("click", () => {
        dropdown.classList.add("dropdown-show");
    });
});

let closeDropdown = document.querySelector(".dropdown-close");
closeDropdown.addEventListener("click", () => {
    dropdown.classList.remove("dropdown-show")
});

// When hamburger menu is clicked show side nav bar
let hamburger = document.querySelector(".hamburger");
let navSide = document.querySelector(".side-nav");
let closeNav = document.querySelector(".nav-close");
let sideMenu = document.querySelector(".side-nav-menu");
hamburger.addEventListener("click", () => {
    navSide.classList.add("show-side-nav");
    sideMenu.classList.add("side-menu-open");
    sideMenu.classList.remove("side-menu-close");
});

closeNav.addEventListener("click", () => {
    sideMenu.classList.remove("side-menu-open");
    sideMenu.classList.add("side-menu-close");

    setTimeout(() => {
        navSide.classList.remove("show-side-nav");
    }, 500);
});