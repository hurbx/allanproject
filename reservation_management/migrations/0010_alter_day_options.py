# Generated by Django 4.2.7 on 2023-11-12 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_management', '0009_tour_mobilization_alter_client_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='day',
            options={'verbose_name': 'Day', 'verbose_name_plural': 'Days'},
        ),
    ]