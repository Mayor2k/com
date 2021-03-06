# Generated by Django 3.1.4 on 2021-08-19 00:08

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210818_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('Холодные закуски', 'Холодные закуски'), ('Салаты', 'Салаты'), ('Хлеб', 'Хлеб'), ('Горячие закуски', 'Горячие закуски'), ('Супы', 'Супы'), ('Основные блюда', 'Основные блюда'), ('Шашлыки', 'Шашлыки'), ('Соусы', 'Соусы'), ('Гарниры', 'Гарниры'), ('Пасты и ризотто', 'Пасты и ризотто'), ('Десерты', 'Десерты')], max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='title',
            field=models.CharField(default=api.models.Order.generate_random_code, max_length=20),
        ),
    ]
