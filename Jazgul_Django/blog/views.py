from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Первый проект на джанго для Жагуль</h1>")


def posters(request):
    post = models.Poster.objects.all()
    return render(request, 'post.html', {'posts': post})