from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.movie_view, name='movie'),
    path('films_detail/<int:id>/', views.movie_detail_view, name='movie_detail'),
]