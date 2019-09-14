from django.shortcuts import render
from .models import Category
from .forms import NewCatForm

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