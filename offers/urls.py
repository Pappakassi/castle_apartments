from django.urls import path
from . import views
from .views import offer_list


urlpatterns = [
    path('submit/<int:apartment_id>/', views.submit_offer, name='submit_offer'),
    path('list/', views.filtered_offer_list, name='offer_list'),
    path('list/', views.offer_list, name='offer_list'),
    path('<int:offer_id>/finalize/contact/', views.finalize_contact, name='finalize_contact'),
    path('<int:offer_id>/finalize/payment/', views.finalize_payment, name='finalize_payment'),
    path('<int:offer_id>/finalize/review/', views.finalize_review, name='finalize_review'),
    path('<int:offer_id>/finalize/confirmation/', views.finalize_confirmation, name='finalize_confirmation'),
]