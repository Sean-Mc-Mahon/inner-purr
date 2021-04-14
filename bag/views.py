from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """" A view to see products placed in bag """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """" A view to add a quantity of a product to bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        #if the item is already in the bag
        if item_id in list(bag.keys()):
            #if another item with the same ID and size exists increment the quantity
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            #if an item with the same ID but different size exists then set the quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        #if the item is NOT already in the bag
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)