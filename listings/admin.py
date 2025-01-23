from django.contrib import admin
from import_export.admin import ExportMixin
from import_export import resources
from .models import Landlord, Property, City, Country, PropertyType



# Экспорт для Landlord
class LandlordResource(resources.ModelResource):
    class Meta:
        model = Landlord
        fields = ('id', 'name', 'email', 'phone')  # Поля для экспорта


# # Админка для Landlord
@admin.register(Landlord)
class LandlordAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = LandlordResource
    list_display = ('id', 'name', 'email', 'phone')  # Поля для отображения
    list_filter = ('name',)  # Фильтрация по email
    search_fields = ('name', 'email', 'phone')  # Поиск
    ordering = ('id',)  # Сортировка


# Экспорт для Property
class PropertyResource(resources.ModelResource):
    class Meta:
        model = Property
        fields = ('id', 'title', 'city', 'property_type', 'room_count', 'price', 'balcony', 'parking', 'wifi', 'landlord__name')


# Админка для Property
@admin.register(Property)
class PropertyAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = PropertyResource
    list_display = ('id', 'title', 'city', 'property_type', 'room_count', 'price', 'balcony', 'parking', 'wifi', 'landlord')
    list_filter = ('city', 'property_type', 'balcony', 'parking', 'wifi', 'landlord')
    search_fields = ('title', 'district', 'landlord__name')
    ordering = ('-price',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)