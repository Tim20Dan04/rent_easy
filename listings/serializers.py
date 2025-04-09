from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'title', 'city', 'district', 'property_type', 'description', 'room_count', 'price', 'balcony', 'parking', 'wifi', 'landlord', 'image']
