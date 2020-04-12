from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView

from ..models.model_school import School
from ..models.model_course import Course
from ..models.model_major import Major
# Create your views here.


class HomeListView(ListView):
    model = School
    template_name = 'home.html'


class SchoolListView(ListView):
    model = School
    template_name = 'school_detail.html'


class MajorListView(ListView):
    model = Major
    template_name = 'major_detail.html'


class CourseListView(ListView):
    model = Course
    template_name = 'course_detail.html'
