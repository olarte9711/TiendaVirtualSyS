from django.contrib import admin
from .models import CarShop, Sale, SaleDetail
# Register your models here.
admin.site.register(CarShop)
admin.site.register(Sale)
admin.site.register(SaleDetail)
