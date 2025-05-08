from django.forms import ModelForm
from django import forms
from apartments.models import Apartment

class ApartmentCreateForm(ModelForm):
    image = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Apartment
        exclude = ['id', 'listing_date', 'is_sold', 'seller']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'street_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'listing_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
