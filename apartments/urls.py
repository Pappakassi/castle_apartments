from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path('', views.apartments_list, name='apartments_list'),
#     path('<int:pk>/', views.apartment_detail, name='apartment_detail'),
# ]

urlpatterns = [
    path('', views.apartments_list, name='apartments_list'),  # ✅ this handles /apartments/
    path('<int:pk>/', views.apartment_detail, name='apartment_detail'),
]
