'''
home_view.py
Chris Meehan
4/13/2020
'''
from django.views.generic import ListView
from ..models.model_school import School


class HomeListView(ListView):
    '''
    This generates the view for the home page.
    '''
    model = School
    template_name = 'home.html'
