from django.urls import path
from . import views

urlpatterns=[
    path('tvshow/', views.show_all, name='tvshow'),
    path('tvshow_detail/<int:id>/', views.show_detail, name='show_detail'),
]