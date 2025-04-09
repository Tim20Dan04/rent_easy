from django.urls import path, include
from . import views
from .views import PropertyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('property_list/', views.property_list, name='property_list'),
    path('tenant-profile/', views.tenant_profile, name='tenant_profile'),  # Профиль арендатора
    path('landlord-profile/', views.landlord_profile, name='landlord_profile'),  # Профиль арендодателя
    path('search/', views.property_search, name='property_search'),
    path('contacts/', views.contacts, name='contacts'),
    path('properties/', views.property_list, name='property_list'),

    path('properties/', views.property_list, name='property_list'),
    path('create/', views.create_property, name='create_property'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

    path('api/', include(router.urls)),
]
