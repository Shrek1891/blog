const toggle = document.querySelector('.navbar-toggle');
const links = document.querySelector('.navbar-links');
const navbar = document.querySelector('.navbar');
const links_menu = links.querySelectorAll('li');

toggle.addEventListener('click', () => {
    navbar.classList.toggle('active');
});


const currentLocation = window.location.href;
console.log(window.location.href );


for (let i = 0; i < links_menu.length; i++) {
    console.log(links_menu[i].querySelector('a').href);
    if (links_menu[i].querySelector('a').href === window.location.href) {
        links_menu[i].classList.add('active');
    }
}
