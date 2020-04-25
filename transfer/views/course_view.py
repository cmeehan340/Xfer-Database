'''
course_view.py
Chris Meehan
4/13/2020
'''
from django.views.generic import (ListView,
                                CreateView,
                                DeleteView,
                                UpdateView,
                                DetailView)
from ..models.model_course import Course
from django.urls import reverse_lazy


class CourseListView(ListView):
    '''
    Generates the view for the courses page
    '''
    model = Course
    template_name = 'course/course_home.html'

class CourseCreateView(CreateView):
    '''
    Generates a view to create courses
    '''
    model = Course
    template_name = 'course/course_new.html'
    fields = '__all__'
    success_url = reverse_lazy('course_home')

class CourseDetailView(DetailView):
    '''
    Generates a view to show course details
    '''
    model = Course
    template_name = 'course/course_detail.html'


class CourseUpdateView(UpdateView):
    '''
    Generates a view to allow updating a course
    '''
    model = Course
    template_name = 'course/course_edit.html'
    success_url = reverse_lazy('course_home')
    fields = '__all__'

class CourseDeleteView(DeleteView):
    '''
    Generates a view to allow deleting a course
    '''
    model = Course
    template_name = 'course/course_delete.html'
    success_url = reverse_lazy('course_home')
