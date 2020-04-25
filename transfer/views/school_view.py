'''
school_view.py
Chris Meehan
4/13/2020
'''
from django.views.generic import (ListView,
                                CreateView,
                                DeleteView,
                                UpdateView,
                                DetailView)
from django.urls import reverse_lazy
from ..models.model_school import School


class SchoolListView(ListView):
    '''
    This generates the view for schools.
    '''
    model = School
    template_name = 'school/school_home.html'


class SchoolDetailView(DetailView):
    model = School
    template_name = 'school/school_detail.html'


class SchoolCreateView(CreateView):

    model = School
    template_name = 'school/school_new.html'
    fields = '__all__'
    success_url = reverse_lazy('school_home')


class SchoolUpdateView(UpdateView):
    model = School
    template_name = 'school/school_edit.html'
    success_url = reverse_lazy('school_home')
    fields = '__all__'


class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'school/school_delete.html'
    success_url = reverse_lazy('school_home')


class SchoolByStateView(ListView):
    '''
    This generates the view for schools.
    '''
    model = School
    template_name = 'school/school_state.html'
