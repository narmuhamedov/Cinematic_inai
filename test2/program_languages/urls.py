from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.prog_lang_view, name='lang'),
    path('index_id/<int:id>/', views.prog_lang_detail_view, name='detail'),
    path('add_prog_lang/', views.add_prog_lang_view, name='add'),
]