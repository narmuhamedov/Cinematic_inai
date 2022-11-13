from django.urls import path
from . import views

urlpatterns = [
    path('man_clothing/', views.clothing_view, name='cl'),
    path('add-cl/', views.add_clothing, name='add'),
]