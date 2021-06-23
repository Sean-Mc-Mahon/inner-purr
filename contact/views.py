from django.shortcuts import render
from .models import EmailContacts, Notice

import os

# Create your views here.


def contact(request):
    """ A view to show contact information """

    addresses = EmailContacts.objects.all()
    notice = Notice.objects.all()
    MAP_KEY = os.getenv('MAP_KEY', '')

    context = {
        'addresses': addresses,
        'notice': notice,
        'page': 'contact',
        'MAP_KEY': MAP_KEY
    }

    return render(request, 'contact/contact.html', context)
