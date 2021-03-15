from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('', views.login),
    path('register/', views.register),
    path('logout', views.logout)
]