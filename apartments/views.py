from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from data import apartments  # this works since data.py is in the root

def apartments_list(request):
    return render(request, 'apartments/apartments_list.html', {'apartments': apartments})

# def home_view(request):
#     return HttpResponse("Hello, World!")

def home_view(request):
    featured_apartments = apartments[:3]  # first 3 only
    return render(request, 'home.html', {'apartments': featured_apartments})

def apartment_detail(request, pk):
    # manually look up apartment by id in the list
    apartment = next((apt for apt in apartments if apt['id'] == pk), None)
    if apartment is None:
        raise Http404("Apartment not found")
    return render(request, 'apartments/apartment_detail.html', {'apartment': apartment})