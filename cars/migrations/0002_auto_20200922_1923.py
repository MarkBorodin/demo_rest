# Generated by Django 3.1.1 on 2020-09-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.IntegerField(choices=[(1, 'Седан'), (2, 'Хэчбек'), (3, 'Универсал'), (4, 'Купе')], verbose_name='Car_Type'),
        ),
    ]