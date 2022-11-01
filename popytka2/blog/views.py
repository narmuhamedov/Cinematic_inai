from django.shortcuts import render
from django.http import HttpResponse
from . import models


def hello_view(request):
    return HttpResponse('Мой номер 0550644770')

def post_car(request):
    car = models.Cars.objects.all()
    return render(request, 'post_car.html', {'car': car})


def about_me(request):
    about = models.About.objects.all()
    return render(request, 'about.html', {'about':about})