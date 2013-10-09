# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from inventory.models import Category, Item
from inventory.forms import EditItemQty, CategoryForm


def index(request):
    categories = Category.objects.all()

    context = {
        'categories' : categories,
    }        

    return render(request, 'inventory/index.html', context)

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    items = Item.objects.filter(category=category)

    context = {
        'category': category,
        'items': items,
    }
    return render(request, 'inventory/detail.html', context)

def item_update(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = EditItemQty(request.POST)
        if form.is_valid():
            # get the form data, create new Post object
            cd = form.cleaned_data
            # adjust the quantity
            item.quantity = cd.get('quantity')
            # save the updated object
            item.save()

            # take them back to the category detail page for the first category that item belongs in
            return HttpResponseRedirect(reverse('inventory:detail', args=(item.category.all()[0].id,)))
    else:
        form = EditItemQty()
        return render(request, 'inventory/edit_item_qty.html', {
            'form' : form,
            'item' : item,
        })

def category_add(request):

    messages = ""
    
    if request.method == 'POST':
        category_form = CategoryForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect('/inventory/')
    else:
        category_form = CategoryForm()
    context = {
        'form': category_form,
        'messages': messages,
    }
    return render(request, 'inventory/category_add.html', context)

def item_qty_get(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return HttpResponse(item.quantity)

