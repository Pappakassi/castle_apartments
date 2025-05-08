document.addEventListener('DOMContentLoaded', function () {
  function registerSearchButtonHandler() {
    const searchButton = document.getElementById('search-icon');
    const searchValueElement = document.getElementById('search-value');
    const apartmentsPlaceholder = document.getElementById('apartment-results');

    searchButton.addEventListener('click', async function () {
      const value = searchValueElement.value;

      const response = await fetch(`/apartments/?search_filter=${encodeURIComponent(value)}`);
      if (response.ok) {
        const json = await response.json();
        const apartments = json.data.map(apartment => `
          <div class="card text-center mb-3" style="width: 18rem;">
            <div class="image" style="background-image: url(${apartment.image}); height: 180px; background-size: cover;"></div>
            <div class="card-body">
              <h5 class="card-title">${apartment.title}</h5>
              <h6><span class="badge text-bg-secondary">${apartment.type}</span></h6>
              <p class="lead">${apartment.listing_price} ISK</p>
              <p>${apartment.city}, ${apartment.postal_code}</p>
              <a href="/apartments/${apartment.id}" class="btn btn-primary">See more</a>
              <a href="/apartments/${apartment.id}/edit/" class="btn btn-secondary">Update</a>
              <a href="/apartments/${apartment.id}/delete/" class="btn btn-danger">Delete</a>
            </div>
          </div>
        `);

        apartmentsPlaceholder.innerHTML = apartments.join('');
      }
    });
  }

  registerSearchButtonHandler();
});
