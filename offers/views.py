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
from django.shortcuts import render, get_object_or_404, redirect
from .models import PurchaseOffer, ContactInfo, Payment, CreditCardPayment, BankTransferPayment, MortgagePayment
from .forms import ContactInfoForm, PaymentForm, CreditCardPaymentForm, BankTransferPaymentForm, MortgagePaymentForm

@login_required
def finalize_contact(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, id=offer_id, buyer=request.user, status__in=['accepted', 'contingent'])

    form = ContactInfoForm(request.POST or None, instance=offer.contact_info)

    if request.method == 'POST' and form.is_valid():
        contact_info = form.save()
        offer.contact_info = contact_info
        offer.save()
        return redirect('finalize_payment', offer_id=offer.id)

    return render(request, 'offers/finalize_contact.html', {'form': form, 'offer': offer})


@login_required
def finalize_payment(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, id=offer_id, buyer=request.user)

    payment_form = PaymentForm(request.POST or None)
    credit_form = CreditCardPaymentForm(request.POST or None)
    bank_form = BankTransferPaymentForm(request.POST or None)
    mortgage_form = MortgagePaymentForm(request.POST or None)

    if request.method == 'POST' and payment_form.is_valid():
        payment = payment_form.save()
        offer.payment = payment
        offer.save()

        payment_type = payment.type

        if payment_type == 'credit_card' and credit_form.is_valid():
            credit = credit_form.save(commit=False)
            credit.payment = payment
            credit.save()

        elif payment_type == 'bank_transfer' and bank_form.is_valid():
            bank = bank_form.save(commit=False)
            bank.payment = payment
            bank.save()

        elif payment_type == 'mortgage' and mortgage_form.is_valid():
            mortgage = mortgage_form.save(commit=False)
            mortgage.payment = payment
            mortgage.save()

        return redirect('finalize_review', offer_id=offer.id)

    return render(request, 'offers/finalize_payment.html', {
        'offer': offer,
        'payment_form': payment_form,
        'credit_form': credit_form,
        'bank_form': bank_form,
        'mortgage_form': mortgage_form
    })


@login_required
def finalize_review(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, id=offer_id, buyer=request.user)

    if request.method == 'POST' and 'confirm' in request.POST:
        # Finalize logic here
        return redirect('finalize_confirmation', offer_id=offer.id)

    return render(request, 'offers/finalize_review.html', {'offer': offer})


@login_required
def finalize_confirmation(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, id=offer_id, buyer=request.user)
    return render(request, 'offers/confirmation.html', {'offer': offer})


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
