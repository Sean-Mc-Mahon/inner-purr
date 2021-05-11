from django.contrib import admin
from .models import Sex, Cat

# Register your models here.

class CatAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sex',
        'status',
        'rescued',
        'health_checked',
        'neutered',
        'adopted',
        'microchipped',
        'vaccinated',
        'image',
    )

    ordering = ('rescued',)

class SexAdmin(admin.ModelAdmin):
    list_display = (
        'sex',
    )

admin.site.register(Cat, CatAdmin)
admin.site.register(Sex, SexAdmin)