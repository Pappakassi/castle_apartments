from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.apartments_list, name='apartments_list'),
    path('<int:pk>/', views.apartment_detail, name='apartment_detail'),
    path('create_apartment/', views.create_apartment, name='create_apartment'),
    path('<int:pk>/delete/', views.delete_apartment, name='delete_apartment'), #Arnar er með þetta öfugt, þ.e.a.s. /delete/<int:id>/
    path('<int:pk>/edit/', views.update_apartment, name='update_apartment'),
    path('sellers/<int:pk>/', views.seller_detail, name='seller_detail'),
    path('sellers/list/', views.seller_list, name='seller_list'),

    path('offers/', include('offers.urls')),


]
