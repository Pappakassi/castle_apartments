from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apartments.models import Apartment
from .forms import PurchaseOfferForm
from django.shortcuts import render
from .models import PurchaseOffer
from apartments.models import Apartment
from django.db.models import Q



from .models import (
    PurchaseOffer,
    ContactInfo,
    Payment,
    CreditCardPayment,
    BankTransferPayment,
    MortgagePayment
)
from .forms import (
    ContactInfoForm,
    PaymentForm,
    CreditCardPaymentForm,
    BankTransferPaymentForm,
    MortgagePaymentForm
)

def filtered_offer_list(request):
    search = request.GET.get("search-value", "")
    city = request.GET.get("city", "")
    apt_type = request.GET.get("type", "")

    offers = PurchaseOffer.objects.select_related('apartment', 'apartment__seller')

    if search:
        offers = offers.filter(
            Q(apartment__address__icontains=search) |
            Q(apartment__title__icontains=search) |
            Q(apartment__city__icontains=search) |
            Q(apartment__description__icontains=search)
        )

    if city:
        offers = offers.filter(apartment__city=city)
    if apt_type:
        offers = offers.filter(apartment__type=apt_type)

    return render(request, 'offers/offer_list.html', {'offers': offers})


@login_required
def finalize_contact(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, pk=offer_id)

    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            request.session['contact_info'] = form.cleaned_data
            return redirect('finalize_payment', offer_id=offer_id)
    else:
        initial = request.session.get('contact_info', {})
        form = ContactInfoForm(initial=initial)

    return render(request, 'offers/finalize_contact.html', {'form': form, 'offer_id': offer_id})


@login_required
def finalize_payment(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, pk=offer_id)
    payment_type = request.session.get('payment', {}).get('type')

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        credit_form = CreditCardPaymentForm(request.POST, prefix='credit')
        bank_form = BankTransferPaymentForm(request.POST, prefix='bank')
        mortgage_form = MortgagePaymentForm(request.POST, prefix='mortgage')

        if payment_form.is_valid():
            request.session['payment'] = payment_form.cleaned_data
            payment_type = payment_form.cleaned_data['type']

            if payment_type == 'credit_card' and credit_form.is_valid():
                request.session['payment_details'] = credit_form.cleaned_data
                return redirect('finalize_review', offer_id=offer_id)
            elif payment_type == 'bank_transfer' and bank_form.is_valid():
                request.session['payment_details'] = bank_form.cleaned_data
                return redirect('finalize_review', offer_id=offer_id)
            elif payment_type == 'mortgage' and mortgage_form.is_valid():
                request.session['payment_details'] = mortgage_form.cleaned_data
                return redirect('finalize_review', offer_id=offer_id)
    else:
        payment_form = PaymentForm(initial=request.session.get('payment'))
        credit_form = CreditCardPaymentForm(prefix='credit', initial=request.session.get('payment_details') if payment_type == 'credit_card' else None)
        bank_form = BankTransferPaymentForm(prefix='bank', initial=request.session.get('payment_details') if payment_type == 'bank_transfer' else None)
        mortgage_form = MortgagePaymentForm(prefix='mortgage', initial=request.session.get('payment_details') if payment_type == 'mortgage' else None)

    return render(request, 'offers/finalize_payment.html', {
        'payment_form': payment_form,
        'credit_form': credit_form,
        'bank_form': bank_form,
        'mortgage_form': mortgage_form,
        'offer_id': offer_id,
    })


@login_required
def finalize_review(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, pk=offer_id)
    contact_info = request.session.get('contact_info')
    payment_data = request.session.get('payment')
    payment_details = request.session.get('payment_details')

    if request.method == 'POST':
        contact = ContactInfo.objects.create(**contact_info)
        payment = Payment.objects.create(type=payment_data['type'])

        if payment_data['type'] == 'credit_card':
            CreditCardPayment.objects.create(payment=payment, **payment_details)
        elif payment_data['type'] == 'bank_transfer':
            BankTransferPayment.objects.create(payment=payment, **payment_details)
        elif payment_data['type'] == 'mortgage':
            MortgagePayment.objects.create(payment=payment, **payment_details)

        offer.contact_info = contact
        offer.payment = payment
        offer.save()

        for key in ['contact_info', 'payment', 'payment_details']:
            request.session.pop(key, None)

        return redirect('finalize_confirmation', offer_id=offer_id)

    return render(request, 'offers/finalize_review.html', {
        'contact_info': contact_info,
        'payment': payment_data,
        'payment_details': payment_details,
        'offer_id': offer_id
    })


@login_required
def finalize_confirmation(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, pk=offer_id)
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
