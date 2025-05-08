from django.urls import path
from . import views

urlpatterns = [
    path('', views.apartments_list, name='apartments_list'),  # ✅ this handles /apartments/
    path('<int:pk>/', views.apartment_detail, name='apartment_detail'),
    path('create_apartment/', views.create_apartment, name='create_apartment'),
    path('<int:pk>/delete/', views.delete_apartment, name='delete_apartment'), #Arnar er með þetta öfugt, þ.e.a.s. /delete/<int:id>/
    path('<int:pk>/edit/', views.update_apartment, name='update_apartment'),

]
