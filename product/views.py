from django.shortcuts import render
from .models import *
import random

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

def askBikki(request, *arggs, **kwargs):  
    prompts = ["Dell 9570 has Geforce Graphics, 9370 has Intel Graphics 🚀", "Dell 9370 has 13 inch screen, is compatible and portable 💼"]
    productId1 =kwargs['pk1']
    productId2 =kwargs['pk2']
    product1 = Product.objects.get(sku = productId1)
    product2 = Product.objects.get(sku = productId2)
    revObject1 = Review.objects.filter(product = productId1)
    revObject2 = Review.objects.filter(product = productId2)
    context = {
        "product1" : product1,
        "product2" : product2,
        "reviewObject1": revObject1[0],
        "reviewObject2": revObject2[0],
        "prompt"    : prompts[random.randint(0,1)]
    }
    print(revObject2)
    return render(request, 'askBikki.html', context)