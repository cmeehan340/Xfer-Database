from django.urls import path
from .views.course_view import CourseListView, CourseCreateView
from .views.home_view import HomeListView
from .views.major_view import MajorListView, MajorDetailView, MajorCreateView
from .views.school_view import (SchoolListView,
                            SchoolCreateView,
                            SchoolDetailView,
                            SchoolDeleteView,
                            SchoolUpdateView)
from .views.approver_view import ApproverListView, ApproverCreateView


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('school', SchoolListView.as_view(), name='school_home'),
    path('school/<int:pk>/', SchoolDetailView.as_view(), name='school_detail'),
    path('major', MajorListView.as_view(), name='majors'),
    path('course', CourseListView.as_view(), name='course_detail'),
    path('major/<int:pk>/', MajorDetailView.as_view(), name='major_detail'),
    path('approver', ApproverListView.as_view(), name='approver_detail'),
    path('approver/new', ApproverCreateView.as_view(), name='approver_new'),
    path('school/new', SchoolCreateView.as_view(), name='school_new'),
    path('school/<int:pk>/edit/', SchoolUpdateView.as_view(), name='post_edit'),
    path('course/new', CourseCreateView.as_view(), name='course_new'),
    path('major/new', MajorCreateView.as_view(), name='major_new'),
]
