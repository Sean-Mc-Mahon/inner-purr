from django.shortcuts import render, get_object_or_404
from .models import Cat, Notice

# Create your views here.

def all_cats(request):
    """ A view to show all cats """

    cats = Cat.objects.all()
    notice = Notice.objects.all()

    context = {
        'cats': cats,
        'notice': notice,
    }

    return render(request, 'cats/cats.html', context)

def cat_detail(request, cat_id):
    """" A view to return individual cats """

    cat = get_object_or_404(Cat, pk=cat_id)
    notice = Notice.objects.all()

    context = {
        'cat': cat,
        'notice': notice,
    }

    return render(request, 'cats/cat_detail.html', context)