from django.shortcuts import render, get_object_or_404
from . import models,forms
from django.http import HttpResponse
from django.views import generic

#получение информации (GET)
class TvShowView(generic.ListView):
    template_name = 'tvshow.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()


#get id
class TvShowDetailView(generic.DetailView):
    template_name = 'tvshow_detail.html'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)

#create TvShow
class TvShowCreateView(generic.CreateView):
    template_name = 'add_tv_show.html'
    form_class = forms.TvShowForm
    queryset = models.TvShow.objects.all()
    success_url = '/tvshow/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TvShowCreateView, self).form_valid(form=form)



#update TvShow

class TvShowUpdateView(generic.UpdateView):
    template_name = 'tvshow_update.html'
    form_class = forms.TvShowForm
    success_url = '/tvshow/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)

    def form_valid(self, form):
        return super(TvShowUpdateView, self).form_valid(form=form)



#delete TvShow
class TvShowDeleteView(generic.DeleteView):
    template_name = 'tvdelete.html'
    success_url = '/tvshow/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)






# def show_all(request):
#     show = models.TvShow.objects.all()
#     return render(request, 'tvshow.html', {'show': show})
#
# #получение id
# def show_detail(request, id):
#     show = get_object_or_404(models.TvShow, id=id)
#     return render(request, 'tvshow_detail.html', {'show':show})
#
