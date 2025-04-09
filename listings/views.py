from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Property, TenantProfile, LandlordProfile, City
from .forms import PropertySearchForm, PropertyForm
from django.core.paginator import Paginator
from .serializers import PropertySerializer
from rest_framework import viewsets



def property_list(request):
    properties = Property.objects.all()
    print(f"Объекты недвижимости: {properties.count()}")  # Добавьте вывод количества объектов

    paginator = Paginator(properties, 5)
    page_number = request.GET.get('page')
    print(f"Номер страницы: {page_number}")  # Отладочный вывод

    page_obj = paginator.get_page(page_number)

    return render(request, 'listings/property_list.html', {'page_obj': page_obj})



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


def property_search(request):
    properties = Property.objects.all()  # Получаем все объекты

    # Логика фильтрации (если нужна)
    if request.method == 'GET':
        form = PropertySearchForm(request.GET or None)

        if form.is_valid():
            city = form.cleaned_data.get('city')
            district = form.cleaned_data.get('district')
            property_type = form.cleaned_data.get('property_type')
            room_count = form.cleaned_data.get('room_count')
            price_min = form.cleaned_data.get('price_min')
            price_max = form.cleaned_data.get('price_max')
            balcony = form.cleaned_data.get('balcony')
            parking = form.cleaned_data.get('parking')
            wifi = form.cleaned_data.get('wifi')

            if city:
                properties = properties.filter(city=city)
            if district:
                properties = properties.filter(district__icontains=district)
            if property_type:
                properties = properties.filter(property_type=property_type)
            if room_count:
                properties = properties.filter(room_count=room_count)
            if price_min is not None:
                properties = properties.filter(price__gte=price_min)
            if price_max is not None:
                properties = properties.filter(price__lte=price_max)
            if balcony:
                properties = properties.filter(balcony=True)
            if parking:
                properties = properties.filter(parking=True)
            if wifi:
                properties = properties.filter(wifi=True)

    else:
        form = PropertySearchForm()

    # Пагинация
    paginator = Paginator(properties, 5)  # 5 объектов на странице
    page_number = request.GET.get('page')  # Получаем номер страницы из запроса
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы

    return render(request, 'listings/property_search.html', {'form': form, 'page_obj': page_obj})

def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление после успешного сохранения
    else:
        form = PropertyForm()
    return render(request, 'listings/create_property.html', {'form': form})

def load_cities(request):
    country_id = request.GET.get('country_id')  # Получаем ID страны из запроса
    cities = City.objects.filter(country_id=country_id).order_by('name')  # Фильтруем города
    city_list = [{'id': city.id, 'name': city.name} for city in cities]  # Подготавливаем данные
    return JsonResponse({'cities': city_list})  # Возвращаем данные в формате JSON

# REST

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer