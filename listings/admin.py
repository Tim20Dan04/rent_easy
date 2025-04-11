from django.contrib import admin
from import_export.admin import ExportMixin
from import_export import resources
from .models import Landlord, Property, City, Country, PropertyType
from simple_history.admin import SimpleHistoryAdmin


# Экспорт для Landlord
class LandlordResource(resources.ModelResource):
    class Meta:
        model = Landlord
        fields = ('id', 'name', 'email', 'phone')  # Поля для экспорта


# Админка для Landlord с использованием fields
@admin.register(Landlord)
class LandlordAdmin(SimpleHistoryAdmin, ExportMixin, admin.ModelAdmin):
    resource_class = LandlordResource
    list_display = ('id', 'name', 'email', 'phone')  # Поля для отображения
    list_filter = ('name',)  # Фильтрация по email
    search_fields = ('name', 'email', 'phone')  # Поиск
    ordering = ('id',)  # Сортировка
    short_description = {
        'name': 'Full Name',
        'phone': 'Contact Phone'
    }
    # Используем fields для простого расположения полей
    fields = ('name', 'email', 'phone')  # Все поля отображаются просто на форме


# Экспорт для Property
class PropertyResource(resources.ModelResource):
    class Meta:
        model = Property
        fields = ('id', 'title', 'city', 'property_type', 'room_count', 'price', 'balcony', 'parking', 'wifi', 'landlord__name')


# Админка для Property с использованием fieldsets
@admin.register(Property)
class PropertyAdmin(SimpleHistoryAdmin, ExportMixin, admin.ModelAdmin):
    resource_class = PropertyResource
    list_display = ('id', 'title', 'city', 'property_type', 'room_count', 'price', 'balcony', 'parking', 'wifi', 'landlord')
    list_filter = ('city', 'property_type', 'balcony', 'parking', 'wifi', 'landlord')
    search_fields = ('title', 'district', 'landlord__name')
    ordering = ('-price',)
    short_description = {
        'title': 'Property Title',
        'landlord': 'Landlord Name'
    }
    # Используем fieldsets для более сложной структуры формы
    fieldsets = (
        (None, {
            'fields': ('title', 'city', 'property_type', 'room_count', 'price')
        }),
        ('Additional Info', {
            'fields': ('balcony', 'parking', 'wifi'),
            'classes': ('collapse',)  # Скрыть этот блок
        }),
        ('Owner Info', {
            'fields': ('landlord',),
        }),
        ('Image', {
            'fields': ('image',),  # Правильное добавление поля для изображения
        }),
    )



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    fields = ('name',)
    short_description = {
        'name': 'City Name'
    }


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    fields = ('name',)
    short_description = {
        'name': 'Country Name'
    }


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    fields = ('name',)
    short_description = {
        'name': 'Property Type'
    }
