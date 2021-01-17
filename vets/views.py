from django.shortcuts import render
from urllib import request

# Create your views here.

def welcome(request):
    return render(request, 'index.html')
