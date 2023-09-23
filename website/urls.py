from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forms/', views.forms, name='forms'),
    path('about/', views.about, name='about'),
    path('output', views.output, name='output')
    ]