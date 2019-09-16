from django.test import TestCase

from .models import Category

class TestCategory(TestCase):
    def test_parent_defaults_to_null(self):
        #Should be able to create a category without a parent
        category = Category.objects.create(name='Test')
        self.assertEqual(category.parent, None)
