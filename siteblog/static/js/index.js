const toggle = document.querySelector('.navbar-toggle');
const links = document.querySelector('.navbar-links');
const navbar = document.querySelector('.navbar');
const links_menu = links.querySelectorAll('li');
toggle.addEventListener('click', () => {
    navbar.classList.toggle('active');
});
const currentLocation = window.location.href
let newUrl = currentLocation.split('/').slice(0, -1).join('/')
for (let i = 0; i < links_menu.length; i++) {
    if (links_menu[i].querySelector('a').href === newUrl + '/') {
        links_menu[i].classList.add('active');
    }
}
