from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PurchaseOffer
from apartments.models import Apartment
from .forms import PurchaseOfferForm
from django.shortcuts import render
from offers.models import PurchaseOffer

@login_required
def submit_offer(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id)

    # Check if an offer already exists by this user
    existing_offer = PurchaseOffer.objects.filter(apartment=apartment, buyer=request.user).first()
    if existing_offer:
        messages.warning(request, "You have already submitted an offer for this apartment.")
        return redirect('apartment_detail', apartment.id)

    if request.method == 'POST':
        form = PurchaseOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.apartment = apartment
            offer.buyer = request.user
            offer.status = 'pending'
            offer.save()
            return render(request, 'offers/offer_success.html', {'apartment': apartment})
    else:
        form = PurchaseOfferForm()

    return render(request, 'offers/submit_offer.html', {'form': form, 'apartment': apartment})


def offer_list(request):
    offers = PurchaseOffer.objects.select_related('apartment', 'apartment__seller').all()
    return render(request, 'offers/offer_list.html', {'offers': offers})
