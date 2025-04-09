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
        label="Страна"
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.none(),
        required=False,
        label="Город"
    )

    # При создании формы — динамически обновляем queryset для поля city
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Используем данные из POST/GET
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # некорректный ввод — оставим пустой queryset
        elif self.initial.get('country'):
            # Если у формы передан initial (например, для редактирования)
            country_id = self.initial.get('country').id
            self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')

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

