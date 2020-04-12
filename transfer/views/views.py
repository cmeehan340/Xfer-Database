'''
views.py
Chris Meehan
4/12/2020
'''
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from ..models.model_school import School
from ..models.model_course import Course
from ..models.model_major import Major
# Create your views here.


class HomeListView(ListView):
    '''
    Creates the view for home page
    '''
    model = School
    template_name = 'home.html'


class SchoolListView(ListView):
    '''
    Creates the view to list schools
    '''
    model = School
    template_name = 'school_detail.html'


class MajorListView(ListView):
    '''
    Creates the view to list Majors
    '''
    model = Major
    template_name = 'major_detail.html'


class CourseListView(ListView):
    '''
    Creates the view to list Courses
    '''
    model = Course
    template_name = 'course_detail.html'
