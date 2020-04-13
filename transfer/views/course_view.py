'''
course_view.py
Chris Meehan
4/13/2020
'''
from django.views.generic import ListView
from ..models.model_course import Course


class CourseListView(ListView):
    '''
    Generates the view for the courses page
    '''
    model = Course
    template_name = 'course_detail.html'
