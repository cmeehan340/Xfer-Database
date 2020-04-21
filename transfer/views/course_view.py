'''
course_view.py
Chris Meehan
4/13/2020
'''
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from ..models.model_course import Course
from django.urls import reverse_lazy


class CourseListView(ListView):
    '''
    Generates the view for the courses page
    '''
    model = Course
    template_name = 'course_home.html'

class CourseCreateView(CreateView):
    # creates object in model Major
    model = Course
    template_name = 'course_new.html'
    fields = '__all__'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_edit.html'
    success_url = reverse_lazy('home')
    fields = '__all__'

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('home')
