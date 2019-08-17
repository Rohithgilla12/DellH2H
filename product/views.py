from django.shortcuts import render
from .models import *

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'home.html', {})