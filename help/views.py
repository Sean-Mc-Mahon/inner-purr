from django.shortcuts import render
from .models import Volunteer, Donations, Notice

# Create your views here.

def help(request):
    """ A view to show all volunteering roles """

    roles = Volunteer.objects.all()
    donations = Donations.objects.all()
    notice = Notice.objects.all()

    context = {
        'roles': roles,
        'donations': donations,
        'notice': notice,
        'page': 'help'
    }

    return render(request, 'help/help.html', context)