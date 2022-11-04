from django.shortcuts import render, get_object_or_404
from . import models


#Получение не полной информации
def showview(request):
    show = models.TvShow.objects.all()
    return render(request, 'index.html', {'show': show})


#Получение id фильма
def showdetailview(request, id):
    show = get_object_or_404(models.TvShow, id=id)
    return render(request, 'tv_detail.html', {'show_object': show})