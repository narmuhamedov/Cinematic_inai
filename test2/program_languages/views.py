from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
# Create your views here.
def prog_lang_view(request):
    lang = models.ProgLang.objects.all()
    return render(request, 'index.html', {'lang_object': lang})


#detail

def prog_lang_detail_view(request, id):
        lang = get_object_or_404(models.ProgLang, id=id)
        return render(request, 'prog_detail.html', {'lang': lang})


#create new post from html page
def add_prog_lang_view(request):
    method = request.method
    if method == 'POST':
        form = forms.ProgLangForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлен')
    else:
        form = forms.ProgLangForms()

    return render(request, 'add_prog_lang.html', {'form': form})
