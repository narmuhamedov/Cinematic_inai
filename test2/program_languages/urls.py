from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.prog_lang_view, name='lang'),
    path('add_prog_lang/', views.add_prog_lang_view, name='add'),
]