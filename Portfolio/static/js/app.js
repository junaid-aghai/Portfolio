const threeLineIcon = document.querySelector('nav .three-line i');
const mobileMenu = document.querySelector('nav .mobile-menu');
const closeIcon = document.querySelector('nav .mobile-menu .ri-close-line');
const navLinks = document.querySelectorAll('nav .mobile-menu .nav_btn a');
threeLineIcon.addEventListener('click', function() {
    mobileMenu.style.display = 'block';
});
closeIcon.addEventListener('click', function() {
    mobileMenu.style.display = 'none';
});
navLinks.forEach(link => {
    link.addEventListener('click', function() {
        mobileMenu.style.display = 'none';
    });
});
