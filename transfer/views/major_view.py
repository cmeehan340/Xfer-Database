'''
major_view.py
Chris Meehan
4/13/2020
'''
from ..models.model_major import Major
from django.views.generic import(ListView,
                                CreateView,
                                DeleteView,
                                UpdateView,
                                DetailView)
from django.urls import reverse_lazy


class MajorListView(ListView):
    '''
    This generates the view for majors.
    '''
    model = Major
    template_name = 'major/major_home.html'


class MajorDetailView(DetailView):
    '''
    This will be the view for each major's specific page
    '''
    model = Major
    template_name = 'major/major_detail.html'

class MajorCreateView(CreateView):
    '''
    This will be the view to create a Major
    '''
    model = Major
    template_name = 'major/major_new.html'
    fields = ['major_name']
    success_url = reverse_lazy('major_home')

class MajorDeleteView(DeleteView):
    '''
    This will be the view to delete a major
    '''
    model = Major
    template_name = 'major/major_delete.html'
    success_url = reverse_lazy('major_home')

class MajorUpdateView(UpdateView):
    '''
    This will be the view to update a major
    '''
    model = Major
    template_name = 'major/major_edit.html'
    success_url = reverse_lazy('major_home')
    fields = '__all__'
