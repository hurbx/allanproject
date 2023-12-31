# Generated by Django 4.2.7 on 2023-11-08 23:13

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('b2b', 'B2B'), ('b2c', 'B2C')], max_length=100)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
            managers=[
                ('client', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
            },
            managers=[
                ('hotel', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'HotelRoom',
                'verbose_name_plural': 'HotelRooms',
            },
            managers=[
                ('hotel_room', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Tour',
                'verbose_name_plural': 'Tours',
            },
            managers=[
                ('tour', django.db.models.manager.Manager()),
            ],
        ),
    ]
