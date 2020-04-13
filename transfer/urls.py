from django.urls import path
from .views.course_view import CourseListView
from .views.home_view import HomeListView
from .views.major_view import MajorListView, MajorDetailView
from .views.school_view import SchoolListView


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('school', SchoolListView.as_view(), name='school_detail'),
    path('major', MajorListView.as_view(), name='majors'),
    path('course', CourseListView.as_view(), name='course_detail'),
    path('major/<int:pk>/', MajorDetailView.as_view(), name='major_detail'),
]
