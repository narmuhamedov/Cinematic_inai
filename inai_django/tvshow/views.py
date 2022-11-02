from django.shortcuts import render, get_object_or_404
from . import models

def show_all(request):
    show = models.TvShow.objects.all()
    return render(request, 'tvshow.html', {'show': show})

#получение id
def show_detail(request, id):
    show = get_object_or_404(models.TvShow, id=id)
    return render(request, 'tvshow_detail.html', {'show':show})

