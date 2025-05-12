from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PurchaseOffer
from apartments.models import Apartment
from .forms import PurchaseOfferForm
from django.shortcuts import render
from offers.models import PurchaseOffer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def finalize_offer(request, offer_id):
    return render(request, 'offers/finalize_offer.html')

@login_required
def submit_offer(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id)

    # Try to get an existing offer from this user for this apartment
    offer = PurchaseOffer.objects.filter(apartment=apartment, buyer=request.user).first()

    if request.method == 'POST':
        # If offer exists, update it; otherwise, create a new one
        form = PurchaseOfferForm(request.POST, instance=offer)
        if form.is_valid():
            new_offer = form.save(commit=False)
            new_offer.apartment = apartment
            new_offer.buyer = request.user
            new_offer.save()
            messages.success(request, 'Your purchase offer has been submitted successfully.')
            return redirect('apartment_detail', pk=apartment.pk)
    else:
        form = PurchaseOfferForm(instance=offer)  # Pre-fill form with existing offer if any

    return render(request, 'offers/submit_offer.html', {
        'form': form,
        'apartment': apartment,
        'resubmitting': offer is not None,  # optional: to customize UI
    })


def offer_list(request):
    offers = PurchaseOffer.objects.select_related('apartment', 'apartment__seller').all()
    return render(request, 'offers/offer_list.html', {'offers': offers})
