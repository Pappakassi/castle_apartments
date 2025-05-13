from django import forms
from .models import PurchaseOffer, ContactInfo, Payment, CreditCardPayment, BankTransferPayment, MortgagePayment

class PurchaseOfferForm(forms.ModelForm):
    class Meta:
        model = PurchaseOffer
        fields = ['price', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['address', 'street_name', 'city', 'postal_code', 'country', 'national_id']
        widgets = {
            'country': forms.Select(choices=[('IS', 'Iceland'), ('NO', 'Norway'), ('DK', 'Denmark')])  # Add full list later
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['type']

class CreditCardPaymentForm(forms.ModelForm):
    class Meta:
        model = CreditCardPayment
        fields = ['cardholder_name', 'card_number', 'expiry_date', 'cvc']

class BankTransferPaymentForm(forms.ModelForm):
    class Meta:
        model = BankTransferPayment
        fields = ['account_number']

class MortgagePaymentForm(forms.ModelForm):
    class Meta:
        model = MortgagePayment
        fields = ['provider']
