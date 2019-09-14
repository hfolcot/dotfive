from django import forms
from .models import Category

class NewCatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]

