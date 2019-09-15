from django.shortcuts import render
from .models import Category
from .forms import NewCatForm
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer
# Create your views here.

def categories_view(request):
    categories = Category.objects.all()
    new_category_form = NewCatForm(request.POST or None)
    if new_category_form.is_valid():
        category = new_category_form.save()
        category.save()
    context = {
        'form':new_category_form,
        'categories' : categories
    }
    return render(request, 'categories.html', context=context)

class CategoryApiView(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)