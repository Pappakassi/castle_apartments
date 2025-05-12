from django import forms
from .models import PurchaseOffer

class PurchaseOfferForm(forms.ModelForm):
    class Meta:
        model = PurchaseOffer
        fields = ['price', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }
