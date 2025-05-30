"""
URL configuration for CastleApartments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apartments.views import home_view  # 👈 Import the view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('apartments/', include('apartments.urls')),
    #path('apartments/finalize', include('apartments.urls')),
    path('', home_view, name='home'),  # 👈 Root path shows "Hello, World!"
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ Add this line
    path('users/', include('users.urls')),
    path('offers/', include('offers.urls')),  # ✅ This actually registers finalize_offer

]



