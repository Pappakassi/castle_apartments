# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import BuyerSignUpForm
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #þetta vistar notandann
            return redirect('login')  # or any success page
    else:
        form = UserCreationForm() #þetta er innbyggt í django
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    return render(request, template_name='users/profile.html')


def signup_view(request):
    if request.method == 'POST':
        form = BuyerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            buyer_group, created = Group.objects.get_or_create(name='buyer')
            user.groups.add(buyer_group)
            return redirect('login')  # or redirect to apartment list
    else:
        form = BuyerSignUpForm()
    return render(request, 'users/signup.html', {'form': form})
