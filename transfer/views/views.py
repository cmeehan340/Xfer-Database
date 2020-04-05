from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView

from ..models.models_transfer import School
# Create your views here.

class SchoolListView(ListView):
    model = School
    template_name = 'home.html'
