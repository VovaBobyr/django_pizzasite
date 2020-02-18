from django.contrib import admin
from app4.models import pizzaShop, Pizza, Order

# Register your models here.
admin.site.register(pizzaShop)
admin.site.register(Pizza)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['pizza', 'name', 'phone', 'date']
