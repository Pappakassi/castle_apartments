from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path
from . import views

#app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('favorite/<int:apartment_id>/', views.favorite_apartment, name='favorite'),
    path('unfavorite/<int:apartment_id>/', views.unfavorite_apartment, name='unfavorite'),

]
