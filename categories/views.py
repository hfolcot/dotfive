from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import NewCatForm, NewSubCatForm, EditCatForm
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer
# Create your views here.


@login_required
def categories_view(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        if 'newSub' in request.POST:
            new_sub_category_form = NewSubCatForm(request.POST or None)
            if new_sub_category_form.is_valid():
                category = new_sub_category_form.save()
                category.save()
                messages.success(request, f"New Category Added: " + category.name)
                return redirect(categories_view)
            else:
                messages.error(request, f"There was a problem")
                return redirect(categories_view)
        elif 'newCat' in request.POST:
            print('New cat')
            new_category_form = NewCatForm(request.POST or None)        
            if new_category_form.is_valid():
                category = new_category_form.save()
                category.save()
                messages.success(request, f"New Category Added: " + category.name)
                return redirect(categories_view)
            else:
                messages.error(request, f"There was a problem")
                return redirect(categories_view)
    else:
        new_sub_category_form = NewSubCatForm()
        new_category_form = NewCatForm()
        context = {
            'cat_form':new_category_form,
            'sub_cat_form': new_sub_category_form,
            'categories' : categories
        }
        return render(request, 'categories.html', context=context)

@login_required
def edit_categories_view(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        edit_category_form = EditCatForm(request.POST or None, instance=category)
        if edit_category_form.is_valid():
            edit_category_form.save()
            messages.success(request, f"Category Updated: " + category.name)
            return redirect(categories_view)
        else:
            messages.error(request, f"There was a problem")
            return redirect(categories_view)    
    else:
        initial_data = {
            'name' : category.name,
            'id' : category.id,
            'parent' : category.parent
        }
        edit_category_form = EditCatForm(initial = initial_data)
        context = {
            'form': edit_category_form
        }
        return render(request, 'edit_categories.html', context=context)

class CategoryApiView(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)