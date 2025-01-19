import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rent_easy.settings')
django.setup()
from listings.models import Property, Landlord
from django.contrib.auth.models import User

def populate():
    user = User.objects.create(username="landlord_user", password="securepassword")

    # Создаем тестового арендодателя
    landlord = Landlord.objects.create(
        user=user,
        name="Кирилл Паршиков",
        email="kirill.parshilov@example.com",
        phone="9999999999"
    )

    # Создаем тестовые объекты недвижимости
    Property.objects.create(
        title="Уютная квартира в центре",
        description="Светлая и просторная квартира в центре города. Удобная транспортная развязка.",
        price=50000,
        location="Москва",
        property_type="Квартира",
        landlord=landlord
    )

    Property.objects.create(
        title="Дом с видом на море",
        description="Дом с великолепным видом на море. Отличный выбор для тех, кто любит природу и тишину.",
        price=80000,
        location="Сочи",
        property_type="Дом",
        landlord=landlord
    )

    # Добавьте больше объектов по мере необходимости
    print("База данных успешно заполнена тестовыми данными.")

if __name__ == "__main__":
    populate()
