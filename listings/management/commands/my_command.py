from django.core.management.base import BaseCommand
from listings.models import Property

class Command(BaseCommand):
    help = 'Создаёт 10 тестовых объектов недвижимости'

    def handle(self, *args, **options):
        for i in range(10):
            Property.objects.create(
                title=f"Test Property {i+1}",
                city_id=1,  # Подставь нужный id
                property_type_id=2,
                room_count=2,
                price=1500 + i * 100,
                balcony=True,
                wifi=True,
                parking=False,
                landlord_id=1  # Подставь нужного пользователя
            )
        self.stdout.write(self.style.SUCCESS('✅ 10 объектов успешно добавлены'))
