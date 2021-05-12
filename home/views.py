from django.shortcuts import render
from cats.models import Cat

# Create your views here.

def index(request):
    """" A view to return the index page """
    cats = Cat.objects.all()

    context = {
        'cats': cats,
    }
    return render(request, 'home/index.html', context)
