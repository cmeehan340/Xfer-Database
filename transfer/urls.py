from django.urls import path
from .views.views import dummy

urlpatterns = [
    path('', dummy, name='home')
]
