from django.shortcuts import render
from .models import EmailContacts

# Create your views here.

def contact(request):
    """ A view to show contact information """

    addresses = EmailContacts.objects.all()

    context = {
        'addresses': addresses,
    }

    return render(request, 'contact/contact.html', context)