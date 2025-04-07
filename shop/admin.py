from django.contrib import admin
from .models import Perfume, Order

@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'perfume', 'quantity', 'ordered_at']
    list_filter = ['ordered_at', 'user']
    search_fields = ['user__username', 'perfume__name']
