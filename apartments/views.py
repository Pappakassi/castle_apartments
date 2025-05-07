from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apartments.models import Apartment
from apartments.forms.apartment_create_form import ApartmentCreateForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from apartments.models import Apartment
from apartments.forms.apartment_create_form import ApartmentCreateForm


def update_apartment(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)

    if request.method == "POST":
        form = ApartmentCreateForm(request.POST, instance=apartment)
        if form.is_valid():
            form.save()
            return redirect('apartment_detail', pk=apartment.pk)
    else:
        form = ApartmentCreateForm(instance=apartment)

    return render(request, 'apartments/update_apartment.html', {'form': form, 'apartment': apartment})


@require_POST
def delete_apartment(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    apartment.delete()
    messages.success(request, "Apartment deleted successfully.")
    return redirect('apartments_list')


#@login_required byrjum á að kommenta þetta út
def create_apartment(request):
    if request.method == "POST":
        form = ApartmentCreateForm(request.POST)
        if form.is_valid():
            apartment = form.save(commit=False)
            #apartment.seller = request.user tók þessa línu út svo að hver sem er gæti bætt inn
            apartment.save()
            return redirect('apartments_list')
    else:
        form = ApartmentCreateForm()

    return render(request, 'apartments/create_apartment.html', {'form': form})

# def apartments_list(request):
#     return render(request, 'apartments/apartments_list.html', {'apartment': apartments})

def apartments_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartments/apartments_list.html', {'apartments': apartments})


# def home_view(request):
#     featured_apartments = apartments[:3]  # first 3 only
#     return render(request, 'home.html', {'apartments': featured_apartments})

def home_view(request):
    featured_apartments = Apartment.objects.all()[:3]
    return render(request, 'home.html', {'apartments': featured_apartments})


# def apartment_detail(request, pk):
#     # manually look up apartment by id in the list
#     apartment = next((apt for apt in apartments if apt['id'] == pk), None)
#     if apartment is None:
#         raise Http404("Apartment not found")
#     return render(request, 'apartments/apartment_detail.html', {'apartment': apartment})

def apartment_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    return render(request, 'apartments/apartment_detail.html', {'apartment': apartment})
