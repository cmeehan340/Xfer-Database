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
    fields = ['school_id',
        'subject_no',
        'title',
        'sem_year_taken',
        'expiration_date',
        'approved_status',
        'comment',
        'approver_id'
        ]


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_edit.html'
    success_url = reverse_lazy('home')


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('home')
