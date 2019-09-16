from django.test import TestCase

from . import forms
from .models import Category

class TestNewCategoryForm(TestCase): 
    def test_form_is_valid(self):
        form = forms.NewCatForm(
            {
                'name': 'test category'
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_cannot_be_blank(self):
        form = forms.NewCatForm(
            {
                'name': ''
            }
        )
        self.assertFalse(form.is_valid())

class TestNewSubCategoryForm(TestCase): 
    def setUp(self):
        Category.objects.create(name="parent") #Create a parent object to link subcategory to
    def test_form_is_valid(self):
        form = forms.NewSubCatForm(
            {
                'name': 'test category',
                'parent': 1
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_cannot_be_blank(self):
        form = forms.NewCatForm(
            {
                'name': '',
                'parent': ''
            }
        )
        self.assertFalse(form.is_valid())
