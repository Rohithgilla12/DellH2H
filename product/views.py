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
    revObject = Review.objects.filter(product = pk)
    context = {
        "object" : obj,
        "revObject" : revObject
    }    
    return render(request, 'productDetail.html', context)

def checkedOutConfirm(request, *args, **kwargs):
    sku = kwargs['pk']
    prodcut = Product.objects.get(sku = sku)
    userId = request.user.id
    userObject = User.objects.get(id = userId)
    context = {
        "product" : prodcut,
        "user"    : userObject
    }    
    return render(request, 'orderConfirmation.html', context)