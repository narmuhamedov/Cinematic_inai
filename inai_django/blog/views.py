from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def hello_world(request):
    return HttpResponse('<h1>Hello World</h1>')

def posts(request):
    post = models.Poster.objects.all()
    return render(request, 'post.html', {'post_object':post})