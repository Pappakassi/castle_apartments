from django import forms
from django.forms import ModelForm
from users.models import Buyer

class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        exclude = ['user', 'favorites']  # don't include user or favorites in the form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': forms.TextInput(attrs={'class': 'form-control'}),
        }
