'''
course_view.py
Chris Meehan
4/13/2020
'''
from django.views.generic import ListView, CreateView
from ..models.model_course import Course


class CourseListView(ListView):
    '''
    Generates the view for the courses page
    '''
    model = Course
    template_name = 'course_detail.html'

class CourseCreateView(CreateView):
    # creates object in model Major
    model = Course
    template_name = 'course_new.html'
    fields = [
        'course_name', 'subject_number', 'title',
        'approved_status', 'comments', 'sem_year_taken', 'expiration_date'
        ]
