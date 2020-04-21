'''
major_view.py
Chris Meehan
4/13/2020
'''
from ..models.model_major import Major
from django.views.generic import(ListView,
                                    DetailView,
                                    CreateView,
                                    DeleteView,
                                    UpdateView
                                )
from django.urls import reverse_lazy


class MajorListView(ListView):
    '''
    This generates the view for majors.
    '''
    model = Major
    template_name = 'major_home.html'


class MajorDetailView(DetailView):
    '''
    This will be the view for each major's specific page
    '''
    model = Major
    template_name = 'major_detail.html'

class MajorCreateView(CreateView):
    # creates object in model Major
    model = Major
    template_name = 'major_new.html'
    fields = ['major_name']

class MajorDeleteView(DeleteView):
    model = Major
    template_name = 'major_delete.html'
    success_url = reverse_lazy('home')

class MajorUpdateView(UpdateView):
    model = Major
    template_name = 'major_edit.html'
    success_url = reverse_lazy('home')
    fields = '__all__'
