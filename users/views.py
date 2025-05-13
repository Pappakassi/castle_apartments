# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect
from apartments.models import Apartment
from users.models import Buyer
from django.contrib.auth.decorators import login_required
from users.forms.buyer_form import BuyerForm
from django.contrib import messages  # Add this import at the top




#Favoriting is an action performed by a user (Buyer).
#It's conceptually part of the user's account behavior, not apartment management.
@login_required
def favorite_apartment(request, apartment_id):
    buyer = request.user.buyer
    apartment = get_object_or_404(Apartment, id=apartment_id)
    buyer.favorites.add(apartment)
    return redirect('apartment_detail', pk=apartment.id)  # 🔧 fixed

@login_required
def unfavorite_apartment(request, apartment_id):
    buyer = request.user.buyer
    apartment = get_object_or_404(Apartment, id=apartment_id)
    buyer.favorites.remove(apartment)
    return redirect('apartment_detail', pk=apartment.id)  # 🔧 fixed



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #þetta vistar notandann
            return redirect('login')  # or any success page
    else:
        form = UserCreationForm() #þetta er innbyggt í django
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_view(request):
    buyer = request.user.buyer
    return render(request, 'users/profile.html', {'buyer': buyer})

@login_required
def edit_profile(request):
    buyer = request.user.buyer
    if request.method == 'POST':
        form = BuyerForm(request.POST, instance=buyer)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Failed to update profile. Please correct the errors.')
    else:
        form = BuyerForm(instance=buyer)

    return render(request, 'users/edit_profile.html', {'form': form})