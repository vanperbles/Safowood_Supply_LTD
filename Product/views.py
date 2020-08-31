from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (ListView,DetailView,DeleteView,CreateView,UpdateView)
from Product import models
from .forms import ItemCreateForm
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.forms import CartAddProductForm
from django.views.generic.edit import FormMixin
from .models import Item
from django.shortcuts import render, get_object_or_404, HttpResponse

import json

# Create your views here.

class ItemListView(ListView):
    models =models.Item
    context_object_name = 'items'
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        return models.Item.objects.all()


class ItemDetailView(FormMixin, DetailView):
    models =models.Item
    form_class = CartAddProductForm
    context_object_name = 'item_detail'

    def product_detail(request, id, slug):
        item = get_object_or_404(Item, id=id, slug=slug, available=True)
        cart_product_form = CartAddProductForm()
        context = {
            'item': item,
            'cart_product_form': cart_product_form
        }
        return render(request, 'Product/item_detail.html', context)



    def get_queryset(self):
        return models.Item.objects.all()



class ItemCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    models =models.Item
    redirect_field_name = 'Product/item_detail.html'
    form_class = ItemCreateForm
    template_name = 'Product/item_form.html'

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    models =models.Item
    redirect_field_name = 'Product/item_detail.html'
    form_class = ItemCreateForm
    template_name = 'Product/item_form.html'

    def get_queryset(self):
        return models.Item.objects.all()


class ItemDeleteView(DeleteView):
    model = models.Item

    success_url = reverse_lazy('item:index')


def Search(request):
    try:
        search= request.GET.get('search')

    except:
        search = None
    if search:
        items = Item.objects.filter(name__icontains =search)
        template = 'Product/result.html'
        context = {'query':search,'items':items}
    else:
        template = 'index.html'
        context = {}
    return render(request,template, context)
