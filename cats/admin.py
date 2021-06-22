from django.contrib import admin
from .models import Sex, Cat, Notice


class CatAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sex',
        'status',
        'rescued',
        'health_checked',
        'neutered',
        'adopted',
        'resident',
        'microchipped',
        'vaccinated',
        'image',
    )
    #  Cats in admin view displayed by date rescued
    ordering = ('-rescued',)


class SexAdmin(admin.ModelAdmin):
    list_display = (
        'sex',
    )


class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'notice',
    )

admin.site.register(Cat, CatAdmin)
admin.site.register(Sex, SexAdmin)
admin.site.register(Notice, NoticeAdmin)
