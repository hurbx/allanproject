# Generated by Django 4.2.7 on 2023-11-11 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_management', '0002_tour_client_tour_final_date_tour_hotel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='currency',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='tour',
            name='quantity',
            field=models.IntegerField(default=None),
        ),
    ]