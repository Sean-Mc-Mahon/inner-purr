from django.contrib import admin
from .models import EmailContacts

# Register your models here.

class AddressesAdmin(admin.ModelAdmin):
    list_display = (
        'directory',
        'email',
    )
    ordering = ('directory',)

admin.site.register(EmailContacts, AddressesAdmin)