'''
school_view.py
Chris Meehan
4/13/2020
'''
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from ..models.model_school import School


class SchoolListView(ListView):
    '''
    This generates the view for schools.
    '''
    model = School
    template_name = 'school_home.html'

class SchoolDetailView(DetailView):
    model = School
    template_name = 'school_detail.html'


class SchoolCreateView(CreateView):
    #create view of all the object of model School
    model = School
    template_name = 'school_new.html'
    fields = ['school_name']


class SchoolUpdateView(UpdateView):
    model = School
    template_name = 'school_edit.html'
    success_url = reverse_lazy('home')


class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'school_delete.html'
    success_url = reverse_lazy('home')
