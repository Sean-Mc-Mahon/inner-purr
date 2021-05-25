from django.contrib import admin
from .models import EmailContacts, Notice

# Register your models here.

class AddressesAdmin(admin.ModelAdmin):
    list_display = (
        'directory',
        'email',
    )
    ordering = ('directory',)

class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'notice',
    )

admin.site.register(EmailContacts, AddressesAdmin)
admin.site.register(Notice, NoticeAdmin)