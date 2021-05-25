from django.contrib import admin
from .models import Volunteer, Donations, Notice

# Register your models here.

class VolunteerAdmin(admin.ModelAdmin):
    list_display = (
        'role',
        'description',
    )
    ordering = ('role',)


class DonationsAdmin(admin.ModelAdmin):
    list_display = (
        'donation_option',
        'description',
    )
    ordering = ('donation_option',)

class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'notice',
    )

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Donations, DonationsAdmin)
admin.site.register(Notice, NoticeAdmin)