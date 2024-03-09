document.addEventListener('mousemove', move);
function move(e){
    this.querySelectorAll('.move').forEach(layer =>{
        const speed = layer.getAttribute('data-speed')

        const x = (window.innerWidth - e.pageX*speed)/120
        const y = (window.innerWidth - e.pageY*speed)/120

        layer.style.transform = `translateX(${x}px) translateY(${y}px)`
    })
}


gsap.from('.general', {opacity:0, duration: 1, delay: 0.3, y:30, stagger: 0.2});  
gsap.from('.logo', {opacity:0, duration: 1, delay: 0.5, y:10});
gsap.from('.first .nav-item', {opacity:0, duration: 1, delay: 0.3, y:30, stagger: 0.2});  
gsap.from('.second .nav-item', {opacity:0, duration: 1, delay: 0.5, y:30, stagger: 0.2}); 