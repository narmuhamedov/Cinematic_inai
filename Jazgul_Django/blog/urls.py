from django.urls import path
from . import views

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello world'),
    path('posts/', views.posters, name='posters'),
]
