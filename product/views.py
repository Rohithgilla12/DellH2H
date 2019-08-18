from django.shortcuts import render
from .models import *

# Create your views here.

def home(request, *args, **kwargs):
    qset = Product.objects.values()
    context = {
        "qset":qset
    }
    return render(request, 'home.html', context)

def productDetailView(request, *args, **kwargs):
    pk = kwargs['pk']
    obj = Product.objects.get(sku = pk)
    context = {
        "object" : obj
    }
    return render(request, 'productDetail.html', context)