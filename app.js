// Obtener las imágenes del carrusel
const slides = document.querySelectorAll('.slides .slide');

// Agregar un evento click a las imágenes
for (const slide of slides) {
    slide.addEventListener('click', function() {
        // Abrir la descripción del producto
        window.location.href = slide.getAttribute('href');
    });
}

// Agregar un evento mouseover a las imágenes
for (const slide of slides) {
    slide.addEventListener('mouseover', function() {
        // Agregar la clase active a la imagen
        slide.classList.add('active');
    });

    slide.addEventListener('mouseout', function() {
        // Eliminar la clase active a la imagen
        slide.classList.remove('active');
    });
}
// Obtener los botones de navegación
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

// Agregar un evento click a los botones de navegación
prevButton.addEventListener('click', function() {
    // Ir a la imagen anterior
    slides[slides.length - 1].classList.remove('active');
    slides[slides.length - 2].classList.add('active');
});

nextButton.addEventListener('click', function() {
    // Ir a la imagen siguiente
    slides[0].classList.remove('active');
    slides[1].classList.add('active');
});
// Obtener el intervalo del carrusel
const interval = setInterval(function() {
    // Ir a la siguiente imagen
    slides[slides.length - 1].classList.remove('active');
    slides[0].classList.add('active');
}, 5000);

// Eliminar el intervalo cuando se haga clic en un botón de navegación
prevButton.addEventListener('click', function() {
    clearInterval(interval);
});

nextButton.addEventListener('click', function() {
    clearInterval(interval);
});
$(document).ready(function() {
    // Agregar interacción al pasar el mouse al icono de carrito
    $(".icono-carrito").hover(function() {
      $(this).css("transform", "scale(1.1)");
});
