# Generated by Django 5.1.2 on 2024-11-01 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_landlord_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='listings.landlord', verbose_name='Арендодатель'),
        ),
    ]
