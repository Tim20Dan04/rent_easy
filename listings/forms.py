# listings/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Property

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

class PropertySearchForm(forms.Form):
    city = forms.ChoiceField(choices=Property.PROPERTY_CITY_CHOICES)
    district = forms.CharField(required=False)
    property_type = forms.ChoiceField(
        choices=Property.PROPERTY_TYPE_CHOICES,
        required=False,
    )
    room_count = forms.IntegerField(required=False, min_value=1)
    price_min = forms.DecimalField(required=False, min_value=0, decimal_places=2)
    price_max = forms.DecimalField(required=False, min_value=0, decimal_places=2)
    
    balcony = forms.BooleanField(required=False)
    parking = forms.BooleanField(required=False)
    wifi = forms.BooleanField(required=False)

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'city', 'district', 'property_type', 'room_count', 'price', 'balcony', 'parking', 'wifi', 'landlord', 'image']
