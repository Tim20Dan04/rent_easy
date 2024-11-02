from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('room', 'Комната'),
    ]

    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    property_type = models.CharField("Тип жилья", max_length=50, choices=PROPERTY_TYPE_CHOICES)
    room_count = models.IntegerField("Количество комнат", default=1)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    balcony = models.BooleanField("Балкон", default=False)
    parking = models.BooleanField("Парковка", default=False)
    wifi = models.BooleanField("Wi-Fi", default=False)
    landlord = models.ForeignKey('Landlord', on_delete=models.CASCADE, related_name='properties', verbose_name="Арендодатель")

    def __str__(self):
        return self.title


class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    # любые другие поля

    def __str__(self):
        return self.user.username

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # дополнительные поля для арендатора, если есть

    def __str__(self):
        return self.user.username
    
class property_list(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TenantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username

class LandlordProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)
    license_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.company_name