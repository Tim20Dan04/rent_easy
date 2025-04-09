from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Property, TenantProfile, LandlordProfile, City
from .forms import PropertySearchForm, PropertyForm
from django.core.paginator import Paginator



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


def property_search(request):
    properties = Property.objects.all()  # Начинаем с всех объектов

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
            furnished = form.cleaned_data.get('furnished')
            pets_allowed = form.cleaned_data.get('pets_allowed')
            wifi = form.cleaned_data.get('wifi')

            # Применяем фильтры
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
            if furnished:
                properties = properties.filter(furnished=True)  # Предполагается, что такое поле есть
            if pets_allowed:
                properties = properties.filter(pets_allowed=True)  # Предполагается, что такое поле есть
            if wifi:
                properties = properties.filter(wifi=True)

    else:
        form = PropertySearchForm()

    paginator = Paginator(properties, 6)  # 6 объектов на страницу
    page_number = request.GET.get('page')  # текущая страница из GET-параметра
    page_obj = paginator.get_page(page_number)  # получаем соответствующую страницу

    return render(request, 'listings/property_search.html', {
        'form': form,
        'page_obj': page_obj,
        'properties': page_obj.object_list,  # чтобы не менять шаблон сильно
    })

    return render(request, 'listings/property_search.html', {'form': form, 'properties': properties})

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