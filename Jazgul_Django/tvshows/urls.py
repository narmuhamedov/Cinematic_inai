from django.urls import path
from . import views

urlpatterns = [
    path('tv/', views.showview, name='shows'),
    path('tvdetail/<int:id>/', views.showdetailview, name='detail'),
]