from django.shortcuts import render
from .models import Volunteer, Donations

# Create your views here.

def help(request):
    """ A view to show all volunteering roles """

    roles = Volunteer.objects.all()
    donations = Donations.objects.all()

    context = {
        'roles': roles,
        'donations': donations,
    }

    return render(request, 'help/help.html', context)