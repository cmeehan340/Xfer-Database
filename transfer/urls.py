from django.urls import path

from .views.views import SchoolListView, HomeListView, MajorListView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('school', SchoolListView.as_view(), name='school_detail'),
    path('major', MajorListView.as_view(), name='major_detail')
]
