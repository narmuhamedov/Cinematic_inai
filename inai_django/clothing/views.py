from django.http import HttpResponse
from django.shortcuts import render
from . import models, forms

def clothing_view(request):
    cl = models.ManClothing.objects.all()
    return render(request, 'cl.html', {'cl': cl})


#for add clothing

def add_clothing(request):
    method = request.method
    if method == "POST":
        form = forms.ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлено!')

    else:
        form = forms.ClothingForm()

    return render(request, 'add_cl.html', {'form': form})