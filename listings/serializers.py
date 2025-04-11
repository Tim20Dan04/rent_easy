from rest_framework import serializers
from .models import Property, Landlord

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = '__all__'