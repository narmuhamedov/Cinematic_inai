from django.shortcuts import render, get_object_or_404
from . import models

def movie_view(request):
    film = models.Movies.objects.all()
    return render(request, 'films.html', {'film': film})

def movie_detail_view(request, id):
    film = get_object_or_404(models.Movies, id=id)
    return render(request, 'films_detail.html', {'film': film})