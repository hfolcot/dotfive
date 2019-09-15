from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
	"""
	Convert bug tickets into JSON for the API
	"""
	class Meta:
		model = Category
		fields = (
			'id', 
			'name',
            'parent')
