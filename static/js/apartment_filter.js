document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('search-icon').addEventListener('click', async function () {
    const params = new URLSearchParams({
      search_filter: document.getElementById('search-value').value,
      postal_code: document.getElementById('postal-code').value,
      type: document.getElementById('type').value,
      min_price: document.getElementById('price-from').value,
      max_price: document.getElementById('price-to').value,
      order_by: document.getElementById('order-by').value,
    });

    const response = await fetch(`/apartments/?${params.toString()}`, {
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      }
    });

    const container = document.getElementById("apartment-results");

    if (response.ok) {
      const json = await response.json();

      if (json.data.length === 0) {
        container.innerHTML = "<p>No apartments match the filters.</p>";
      } else {
        container.innerHTML = json.data.map(apt => `
          <div class="card mb-3" style="width: 18rem;">
            <img src="${apt.image || 'https://placehold.co/300x200?text=No+Image'}" class="card-img-top" alt="${apt.title}">
            <div class="card-body">
              <h5 class="card-title">${apt.title}</h5>
              <p class="card-text">${apt.address}, ${apt.city} ${apt.postal_code}</p>
              <p class="card-text">${apt.listing_price} ISK</p>
              <a href="/apartments/${apt.id}" class="btn btn-primary">Details</a>
            </div>
          </div>
        `).join('');
      }
    } else {
      container.innerHTML = "<p>Something went wrong with the search request.</p>";
    }
  });
});
