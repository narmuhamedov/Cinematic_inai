from django.urls import path
from . import views

urlpatterns=[
    path('tvshow/', views.TvShowView.as_view(), name='tvshow'),
    path('tvshow_detail/<int:id>/', views.TvShowDetailView.as_view(), name='show_detail'),
    path('tvshow/<int:id>/update/', views.TvShowUpdateView.as_view(), name='show_detail'),
    path('tvshow/<int:id>/delete/', views.TvShowDeleteView.as_view(), name='show_detail'),

    path('add-shows/', views.TvShowCreateView.as_view(), name='add shows'),
]