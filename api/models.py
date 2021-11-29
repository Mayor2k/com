from django.db import models
from django.core.validators import MinValueValidator
from random import randint

class Order(models.Model):
    def generate_random_code():
        return 'Заказ №%s'%randint(1,9999)

    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    title = models.CharField(default=generate_random_code, max_length=20)
    order = models.JSONField(default=list)
    status = models.CharField(default='accepted', max_length=50, blank=False)
    table = models.PositiveSmallIntegerField(default=1,blank=True,validators=[MinValueValidator(1)])

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

class menuItem(models.Model):
    CHOICES = [
        ('Холодные закуски', 'Холодные закуски'),
        ('Салаты', 'Салаты'),
        ('Хлеб', 'Хлеб'),
        ('Горячие закуски', 'Горячие закуски'),
        ('Супы', 'Супы'),
        ('Основные блюда', 'Основные блюда'),
        ('Шашлыки', 'Шашлыки'),
        ('Соусы', 'Соусы'),
        ('Гарниры', 'Гарниры'),
        ('Пасты и ризотто', 'Пасты и ризотто'),
        ('Десерты', 'Десерты')
    ]

    title = models.CharField(max_length=50, blank=False)
    category = models.CharField(max_length=50, choices=CHOICES, blank=False)
    composition = models.TextField(blank=True)
    note = models.TextField(blank=True)
    price = models.PositiveSmallIntegerField(default=1,blank=True,validators=[MinValueValidator(1)])

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(menuItem, self).save(*args, **kwargs)

