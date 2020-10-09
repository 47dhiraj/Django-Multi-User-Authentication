from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('', views.loginPage, name="login"),
	path('register/', views.clientregisterPage, name="clientregister"),
	path('adminregister/', views.adminregisterPage, name="adminregister"),
	path('clienthome/', views.clienthome, name="clienthome"),
	path('adminhome/', views.adminhome, name="adminhome"),
	path('logoutall/', views.logoutall, name="logoutall"),

]
