gsap.from('.logo', {opacity:0, duration: 1, delay: 0.5, y:10});
gsap.from('.first .nav-item', {opacity:0, duration: 1, delay: 0.5, y:10});
gsap.from('.second .nav-item', {opacity:0, duration: 1, delay: 0.5, y:10});



gsap.from('.container', {opacity:0, duration: 1, delay: 0.5, y:10});
gsap.from('.container .image', {opacity:0, duration: 1, delay: 0.5, y:10});
gsap.from('.new_season', {opacity:0, duration: 1, delay: 0.3, y:1}); 

document.addEventListener('scroll', () => {
    const header = document.querySelector('header');

    if (window.scrollY > 0) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
})

