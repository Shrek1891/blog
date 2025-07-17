const toggle = document.querySelector('.navbar-toggle');
const links = document.querySelector('.navbar-links');
const navbar = document.querySelector('.navbar');

toggle.addEventListener('click', () => {
    console.log('click');
    navbar.classList.toggle('active');
});