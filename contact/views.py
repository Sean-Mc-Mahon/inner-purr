from django.shortcuts import render
from .models import EmailContacts, Notice

# Create your views here.


def contact(request):
    """ A view to show contact information """

    addresses = EmailContacts.objects.all()
    notice = Notice.objects.all()

    context = {
        'addresses': addresses,
        'notice': notice,
        'page': 'contact'
    }

    return render(request, 'contact/contact.html', context)
