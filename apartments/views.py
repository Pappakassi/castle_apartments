from .models import Seller, Apartment
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from offers.models import PurchaseOffer

from django.http import JsonResponse
from .models import Apartment
from django.db.models import Q
from apartments.forms.apartment_create_form import ApartmentCreateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Seller

# View to display a list of all sellers
def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'apartments/seller_list.html', {'sellers': sellers})

# View to show details of a specific seller and the apartments they have for sale
def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    apartments = seller.apartment_set.filter(is_sold=False)
    return render(request, 'apartments/seller_detail.html', {
        'seller': seller,
        'apartments': apartments,
    })

# View to update an existing apartment (accessible only by logged-in users)
@login_required
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

# View to delete an apartment (POST-only, logged-in users)
@login_required
@require_POST
def delete_apartment(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk) #Arnar notar id=id í sínum kóða
    apartment.delete()
    messages.success(request, "Apartment deleted successfully.")
    return redirect('apartments_list') #þetta segir hvert við förum eftir delete

# View to create a new apartment listing (accessible only by logged-in users)
@login_required
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

# View to list all apartments with support for filtering, searching, sorting, and API response
def apartments_list(request):
    apartments = Apartment.objects.all()
    search = request.GET.get('search_filter')

    # Search by street name (case-insensitive)
    search = request.GET.get('search_filter')
    if search:
        apartments = apartments.filter(address__icontains=search)

    # Filter by postal code
    postal_code = request.GET.get('postal_code')
    if postal_code:
        apartments = apartments.filter(postal_code=postal_code)

    # Filter by type (apartment, villa, etc.)
    apt_type = request.GET.get('type')
    if apt_type:
        apartments = apartments.filter(type__iexact=apt_type)

    # Filter by price range
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        apartments = apartments.filter(listing_price__gte=min_price)
    if max_price:
        apartments = apartments.filter(listing_price__lte=max_price)

    # Order by price or name
    order_by = request.GET.get('order_by')
    if order_by in ['listing_price', 'title']:
        apartments = apartments.order_by(order_by)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.headers.get(
            'accept') == 'application/json':
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
            } for apt in apartments]
        })

    return render(request, 'apartments/apartments_list.html', {
        'apartments': apartments,
    })


# View for rendering the home page and showing 3 featured apartments
def home_view(request):
    apartments_qs = Apartment.objects.all()
    featured_apartments = apartments_qs[:3]
    return render(request, 'home.html', {
        'apartments': featured_apartments,
        'apartment': apartments_qs.first(),  # get the first apartment before slicing
    })

# View to display a specific apartment's details (including any existing offer by the logged-in user)
def apartment_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)

    offer = None
    if request.user.is_authenticated:
        offer = PurchaseOffer.objects.filter(apartment=apartment, buyer=request.user).first()

    return render(request, 'apartments/apartment_detail.html', {
        'apartment': apartment,
        'offer': offer,  # send full offer object (or None)
    })


