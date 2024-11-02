from django.shortcuts import render, get_object_or_404
from .models import Property, TenantProfile, LandlordProfile


def property_list(request):
    properties = Property.objects.all()
    print("Представление вызвано")  # Добавьте эту строку
    return render(request, 'listings/property_list.html', {'properties': properties})

# def property_list(request):
#     properties = Property.objects.all()  # Извлечение всех объектов Property
#     return render(request, 'listings/housing.html', {'properties': properties})


def home(request):
    properties = Property.objects.all()[:5]  # Примеры жилья
    return render(request, 'listings/home.html', {'properties': properties})

def search(request):
    # Логика поиска
    return render(request, 'listings/search.html')

def listing_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'listings/listing_detail.html', {'property': property})


def contacts(request):
    return render(request, 'listings/contact.html')



def tenant_profile(request):
    tenant_profile = TenantProfile.objects.first()  # Получение первого профиля арендатора
    return render(request, 'listings/tenant_profile.html', {'profile': tenant_profile})

def landlord_profile(request):
    landlord_profile = LandlordProfile.objects.first()  # Получение первого профиля арендодателя
    return render(request, 'listings/landlord_profile.html', {'profile': landlord_profile})


