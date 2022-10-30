from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('posts/', views.posts, name='posts'),
    path('about_us/', views.about, name='about'),
    path('contacts/', views.contacs, name='contact'),
]
