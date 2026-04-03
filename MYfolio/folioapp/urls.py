

"""
URL configuration for MYfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
#folioapp/urls.py
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
path('about/', views.about, name='about'),
    path('starter/', views.starter, name='starter'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.servicespage, name='service'),
    path('index/', views.index, name='index'),
    path('', views.portfolio, name='portfolio'),
    path('portfoliodetails/', views.portfoliopage, name='portfoliodetails'),
    path('resume/', views.resume, name='resume.'),
    path('servicedetails/', views.servicespage, name='servicedetails'),
    ]