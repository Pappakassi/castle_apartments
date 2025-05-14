document.addEventListener('DOMContentLoaded', function () {
  const carouselElement = document.querySelector('#carouselExampleCaptions');
  const toggleBtn = document.getElementById('carousel-toggle');
  const carousel = bootstrap.Carousel.getOrCreateInstance(carouselElement);

  let isPaused = false;

  toggleBtn.addEventListener('click', function () {
    if (isPaused) {
      carousel.cycle(); // resume autoplay
      toggleBtn.innerHTML = '⏸️ Pause';
    } else {
      carousel.pause(); // stop autoplay
      toggleBtn.innerHTML = '▶️ Play';
    }
    isPaused = !isPaused;
  });
});