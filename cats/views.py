from django.shortcuts import render, get_object_or_404
from .models import Cat

# Create your views here.

def all_cats(request):
    """ A view to show all cats """

    cats = Cat.objects.all()

    context = {
        'cats': cats,
    }

    return render(request, 'cats/cats.html', context)

def cat_detail(request, cat_id):
    """" A view to return individual cats """

    cat = get_object_or_404(Cat, pk=cat_id)

    context = {
        'cat': cat,
    }

    return render(request, 'cats/cat_detail.html', context)