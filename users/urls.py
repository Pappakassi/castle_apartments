from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='users_test'),
    path('signup/', views.signup_view, name='signup'),
    path('register/', views.register, name='register'),
]