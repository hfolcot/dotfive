from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.CategoryApiView)

urlpatterns = [
	path('api/', include(router.urls)),
	path('api/auth', include('rest_framework.urls')),
]