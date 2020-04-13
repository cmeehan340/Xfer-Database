'''
major_view.py
Chris Meehan
4/13/2020
'''
from ..models.model_major import Major
from django.views.generic import ListView


class MajorListView(ListView):
    '''
    This generates the view for majors.
    '''
    model = Major
    template_name = 'major_detail.html'
