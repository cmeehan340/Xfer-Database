from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dummy(request):
    return HttpResponse('Hello, World!')
