# rent_easy/listings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property_list/', views.property_list, name='property_list'),
    path('tenant-profile/', views.tenant_profile, name='tenant_profile'),  # Профиль арендатора
    path('landlord-profile/', views.landlord_profile, name='landlord_profile'),  # Профиль арендодателя
    path('search/', views.search, name='search'),
    path('contacts/', views.contacts, name='contacts'),

    path('properties/', views.property_list, name='property_list'),
]
