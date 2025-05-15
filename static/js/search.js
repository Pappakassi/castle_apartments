document.addEventListener('DOMContentLoaded', function () {
  const fields = ['#search-value', '#postal-code', '#type', '#price-from', '#price-to', '#order-by'];
  const resultsContainer = document.getElementById('results'); // Make sure this exists

  fields.forEach(selector => {
    document.querySelector(selector).addEventListener('input', liveSearch);
  });

  function liveSearch() {
    const params = new URLSearchParams({
      search_filter: document.querySelector('#search-value').value,
      postal_code: document.querySelector('#postal-code').value,
      type: document.querySelector('#type').value,
      min_price: document.querySelector('#price-from').value,
      max_price: document.querySelector('#price-to').value,
      order_by: document.querySelector('#order-by').value,
    });

    fetch(`/apartments/?${params.toString()}`, {
      headers: { 'X-Requested-With': 'XMLHttpRequest' }
    })
    .then(res => res.json())
    .then(data => {
      resultsContainer.innerHTML = '';
      data.data.forEach(apartment => {
        resultsContainer.innerHTML += `
          <div class="card my-2 p-3">
            <h5>${apartment.title}</h5>
            <p>${apartment.address}, ${apartment.postal_code} - ${apartment.type}</p>
            <strong>${apartment.listing_price} ISK</strong>
          </div>`;
      });
    });
  }
});