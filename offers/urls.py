from django.urls import path
from . import views
from .views import offer_list

urlpatterns = [
    path('submit/<int:apartment_id>/', views.submit_offer, name='submit_offer'),
    path('list/', offer_list, name='offer_list'),
]
