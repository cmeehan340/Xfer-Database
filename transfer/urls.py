from django.urls import path

from .views.views import SchoolListView

urlpatterns = [
    path('', SchoolListView.as_view(), name='home')
]
