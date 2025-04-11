from rest_framework import serializers
from .models import Property, Landlord

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

    def validate_price(self, value):
        if value < 1001:
            raise serializers.ValidationError("Цена должна быть минимум 1001.")
        return value

    def validate(self, data):
        has_balcony = data.get('balcony', False)
        has_wifi = data.get('wifi', False)
        has_parking = data.get('parking', False)

        if not (has_balcony or has_wifi or has_parking):
            raise serializers.ValidationError(
                "Должен быть выбран хотя бы один из параметров: балкон, Wi-Fi или парковка."
            )

        return data

class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = '__all__'