from django.contrib import admin
from .models import Volunteer, Donations

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

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Donations, DonationsAdmin)