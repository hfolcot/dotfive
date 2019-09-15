from django import forms
from .models import Category

class NewCatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]

class NewSubCatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'parent'
        ]
        widgets = {'parent':forms.HiddenInput}

class EditCatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'parent',
            'id'
        ]
        widgets = {'id':forms.HiddenInput}