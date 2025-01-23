from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):

    title = models.CharField("Название", max_length=100)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='cities')
    # city = models.CharField("Город", max_length=255, default="Moscow", choices=PROPERTY_CITY_CHOICES)
    district = models.TextField("Район", max_length=255, default=False)
    property_type = models.ForeignKey("PropertyType", on_delete=models.CASCADE, related_name='property_type', verbose_name="Тип жилья", default=0, null=False)
    description = models.TextField("Описание")
    room_count = models.IntegerField("Количество комнат", default=1)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    balcony = models.BooleanField("Балкон", default=False)
    parking = models.BooleanField("Парковка", default=False)
    wifi = models.BooleanField("Wi-Fi", default=False)
    landlord = models.ForeignKey('Landlord', on_delete=models.CASCADE, related_name='properties', verbose_name="Арендодатель", default=0)
    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"

class PropertyType(models.Model):
    name = models.CharField("Тип жилья", max_length=50)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField("Страна",  max_length=100)

    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField("Город", max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return f"{self.name} {self.country.name}"

class Landlord(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="landlord_profile")
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    # любые другие поля

    def __str__(self):
        return self.name

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