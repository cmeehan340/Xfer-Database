'''
major_view.py
Chris Meehan
4/13/2020
'''
from ..models.model_major import Major
from django.views.generic import ListView, DetailView


class MajorListView(ListView):
    '''
    This generates the view for majors.
    '''
    model = Major
    template_name = 'majors.html'


class MajorDetailView(DetailView):
    '''
    This will be the view for each major's specific page
    '''
    model = Major
    template_name = 'major_detail.html'
