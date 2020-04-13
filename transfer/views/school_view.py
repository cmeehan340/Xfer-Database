'''
school_view.py
Chris Meehan
4/13/2020
'''
from django.views.generic import ListView
from ..models.model_school import School


class SchoolListView(ListView):
    '''
    This generates the view for schools.
    '''
    model = School
    template_name = 'school_detail.html'
