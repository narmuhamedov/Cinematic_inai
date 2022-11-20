from django.shortcuts import render
from . import models


def blog_view(request):
    film = models.Film.objects.all()
    post = models.Poster.objects.all()
    food = models.Food.objects.all()
    context = {
        'film': film,
        'post': post,
        'food': food
    }
    return render(request, 'index.html', context)
