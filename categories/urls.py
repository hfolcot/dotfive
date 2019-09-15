from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.CategoryApiView)

urlpatterns = [
	path('edit/<int:id>', views.edit_categories_view, name="edit"),
	path('api/', include(router.urls)),
	path('api/auth', include('rest_framework.urls')),
]