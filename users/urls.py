from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('test/', views.test_view, name='users_test'),
    path('signup/', views.signup_view, name='signup'),
    path('register/', views.register, name='register'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile', views.profile, name='profile'),

]
