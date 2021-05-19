from django.contrib import admin
from .models import Drink, Food, Treats

# Register your models here.

class DrinkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )
    ordering = ('name',)


class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )
    ordering = ('name',)


class TreatsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )
    ordering = ('name',)


admin.site.register(Drink, DrinkAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Treats, TreatsAdmin)