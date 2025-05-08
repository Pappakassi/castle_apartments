from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apartments.models import Apartment
from apartments.forms.apartment_create_form import ApartmentCreateForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from apartments.models import Apartment
from apartments.forms.apartment_create_form import ApartmentCreateForm

from django.http import JsonResponse
from django.shortcuts import render
from .models import Apartment


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
    apartment = get_object_or_404(Apartment, pk=pk) #Arnar notar id=id í sínum kóða
    apartment.delete()
    messages.success(request, "Apartment deleted successfully.")
    return redirect('apartments_list') #þetta segir hvert við förum eftir delete


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
#     if 'search_filter' in request.GET:
#         return JsonResponse({
#             'data' : [{
#                 'id' : x.id,
#                 'name' : x.name,
#                 'price' : x.price,
#                 'description' : x.description,
#                 'category' : x.category.name,
#
#             }] for x in Apartment.objects.filter(name__icontains=request.GET['search_filter']).order_by('name')
#         })
#     apartments = Apartment.objects.all()
#     return render(request, 'apartments/apartments_list.html', {'apartments': apartments})

def apartments_list(request):
    if 'search_filter' in request.GET: #ef það er search filter í get request'unni þá viljum við gera eitthvað
        return JsonResponse({
            'data': [{
                'id': apt.id,
                'title': apt.title,
                'address': apt.address,
                'city': apt.city,
                'postal_code': apt.postal_code,
                'description': apt.description,
                'type': apt.type,
                'listing_price': apt.listing_price,
                'image': apt.image,
            } for apt in Apartment.objects.filter(title__icontains=request.GET['search_filter']).order_by('title')]
        })

    apartments = Apartment.objects.all()
    return render(request, 'apartments/apartments_list.html', {'apartments': apartments})

# def apartments_list(request):
#     apartments = Apartment.objects.all()
#     return render(request, 'apartments/apartments_list.html', {'apartments': apartments})


def home_view(request):
    featured_apartments = Apartment.objects.all()[:3] #sækir fyrstu þrjár íbúðirnar
    return render(request, 'home.html', {'apartments': featured_apartments})

def apartment_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    return render(request, 'apartments/apartment_detail.html', {'apartment': apartment})
