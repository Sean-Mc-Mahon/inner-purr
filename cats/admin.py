from django.contrib import admin
from .models import Status, Sex, Cat

# Register your models here.

class CatAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sex',
        'status',
        'image',
    )

    ordering = ('name',)

# class StatusAdmin(admin.ModelAdmin):
#     list_display = (
#         'status',
#     )

class SexAdmin(admin.ModelAdmin):
    list_display = (
        'sex',
    )

admin.site.register(Cat, CatAdmin)
# admin.site.register(Status, StatusAdmin)
admin.site.register(Sex, SexAdmin)