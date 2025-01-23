# listings/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Property, Country, City, PropertyType

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class PropertySearchForm(forms.Form):
#     country = forms.ModelChoiceField(
#         queryset = Country.objects.all(),
#         required = False,
#         label="Страна"
#     )
#     city = forms.ModelChoiceField(
#         queryset = City.objects.all(),
#         required = False,
#         label="Город"
#     )

class PropertySearchForm(forms.Form):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        required=False,
        label="Страна",
        widget=forms.Select(attrs={'id': 'id_country'})  # ID для JavaScript
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.none(),  # Начальный пустой queryset
        required=False,
        label="Город",
        widget=forms.Select(attrs={'id': 'id_city'})  # ID для JavaScript
    )

    district = forms.CharField(required=False, label="Район")
    property_type = forms.ModelChoiceField(
        queryset = PropertyType.objects.all(),  # Все типы жилья из модели PropertyType
        required = False,
        label="Тип жилья"
    )
    room_count = forms.IntegerField(required=False, min_value=1, label="Количество комнат")
    price_min = forms.DecimalField(required=False, min_value=0, decimal_places=2, label="Минимальная цена")
    price_max = forms.DecimalField(required=False, min_value=0, decimal_places=2, label="Максимальная цена")
    
    balcony = forms.BooleanField(required=False, label="Балкон")
    parking = forms.BooleanField(required=False, label="Парковка")
    wifi = forms.BooleanField(required=False, label="Wi-Fi")

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'city', 'district', 'property_type', 'room_count', 'price', 'balcony', 'parking', 'wifi', 'landlord', 'image']
