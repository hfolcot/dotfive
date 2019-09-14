from django.contrib.auth import views as auth_views
from django.urls import path
from .views import registration_view

urlpatterns = [
	path('register', registration_view, name="register"),
	path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
	path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login')

]