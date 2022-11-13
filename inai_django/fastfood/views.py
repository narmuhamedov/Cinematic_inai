from django.shortcuts import render
from . import models, forms
from django.http import HttpResponse

def order_view(request):
    order = models.Order.objects.all()
    return render(request, 'fasfood.html', {'order': order})

#add FastFood

def add_food_view(request):
    method = request.method
    if method == 'POST':
        form = forms.FasFoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<center><b>Ваш заказ принят!</b></center>')
    else:
        form = forms.FasFoodForm()

    return render(request, 'add_fastfood.html', {'form': form})
