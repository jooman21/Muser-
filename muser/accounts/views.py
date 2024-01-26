from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def testpage(request):
    
    return render (request, 'login.html')

