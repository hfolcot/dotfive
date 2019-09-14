from django.shortcuts import render
from .models import Category

# Create your views here.

def categories_view(request):
    #categories = Categories.objects.get()
    return render(request, 'categories.html')