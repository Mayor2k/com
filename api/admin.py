from django.contrib import admin
from .models import Order, menuCategory, menuItem

admin.site.register(Order)
admin.site.register(menuItem)
admin.site.register(menuCategory)