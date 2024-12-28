from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'year', 'selling_price', 'present_price', 'fuel_type', 'seller_type', 'transmission', 'owner')
    search_fields = ('car_name', 'fuel_type', 'seller_type')
    list_filter = ('fuel_type', 'seller_type', 'transmission')
