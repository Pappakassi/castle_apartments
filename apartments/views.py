from .models import Seller, Apartment
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from offers.models import PurchaseOffer




def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    apartments = seller.apartment_set.filter(is_sold=False)
    return render(request, 'apartments/seller_detail.html', {
        'seller': seller,
        'apartments': apartments,
    })

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

def home_view(request):
    featured_apartments = Apartment.objects.all()[:3] #sækir fyrstu þrjár íbúðirnar
    return render(request, 'home.html', {'apartments': featured_apartments})

# def apartment_detail(request, pk):
#     apartment = get_object_or_404(Apartment, pk=pk)
#     return render(request, 'apartments/apartment_detail.html', {'apartment': apartment})

def apartment_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)

    offer_exists = False
    if request.user.is_authenticated:
        offer_exists = PurchaseOffer.objects.filter(apartment=apartment, buyer=request.user).exists()

    return render(request, 'apartments/apartment_detail.html', {
        'apartment': apartment,
        'offer_exists': offer_exists,
    })