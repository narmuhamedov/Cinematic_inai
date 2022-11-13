from django.urls import path
from . import views

urlpatterns = [
    path('fast_food/', views.order_view, name='order'),
    path('add_fast_food/', views.add_food_view, name='add'),
]