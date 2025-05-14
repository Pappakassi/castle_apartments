document.addEventListener('DOMContentLoaded', function () {
  const triggers = document.querySelectorAll('.open-modal');
  const modal = new bootstrap.Modal(document.getElementById('carouselModal'));
  const modalCarousel = document.getElementById('modalCarousel');

  triggers.forEach(trigger => {
    trigger.addEventListener('click', function () {
      const index = parseInt(this.getAttribute('data-index'));

      // Show modal
      modal.show();

      // Reset active slide in modal carousel
      const items = modalCarousel.querySelectorAll('.carousel-item');
      const indicators = modalCarousel.querySelectorAll('[data-bs-slide-to]');

      items.forEach((item, i) => {
        item.classList.remove('active');
        if (i === index) item.classList.add('active');
      });

      if (indicators.length) {
        indicators.forEach((btn, i) => {
          btn.classList.remove('active');
          if (i === index) btn.classList.add('active');
        });
      }
    });
  });
});

// thumbnail fix for carousel
document.addEventListener('DOMContentLoaded', function () {
  const mainCarousel = document.getElementById('carouselExampleCaptions');
  const thumbnailButtons = document.querySelectorAll('.carousel-thumb');

  mainCarousel.addEventListener('slid.bs.carousel', function (e) {
    const activeIndex = e.to;

    // Remove 'active' from all thumbnails
    thumbnailButtons.forEach(btn => btn.classList.remove('active'));

    // Add 'active' to the matching thumbnail
    if (thumbnailButtons[activeIndex]) {
      thumbnailButtons[activeIndex].classList.add('active');
    }
  });
});