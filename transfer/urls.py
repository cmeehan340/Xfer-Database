from django.urls import path
from .views.course_view import (CourseListView,
                                CourseCreateView,
                                CourseDeleteView,
                                CourseUpdateView,
                                CourseDetailView)
from .views.home_view import HomeListView
from .views.major_view import MajorListView, MajorDetailView, MajorCreateView
from .views.school_view import (SchoolListView,
                            SchoolCreateView,
                            SchoolDetailView,
                            SchoolDeleteView,
                            SchoolUpdateView)
from .views.approver_view import (ApproverListView,
                            ApproverCreateView,
                            ApproverDetailView,
                            ApproverDeleteView,
                            ApproverUpdateView)
from .views.approver_view import ApproverListView, ApproverCreateView


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('school', SchoolListView.as_view(), name='school_home'),
    path('school/<int:pk>', SchoolDetailView.as_view(), name='school_detail'),
    path('school/new', SchoolCreateView.as_view(), name='school_new'),
    path('school/<int:pk>/edit', SchoolUpdateView.as_view(), name='school_edit'),
    path('school/<int:pk>/delete', SchoolDeleteView.as_view(), name='school_delete'),
    path('major', MajorListView.as_view(), name='majors'),
    path('major/<int:pk>', MajorDetailView.as_view(), name='major_detail'),
    path('major/new', MajorCreateView.as_view(), name='major_new'),
    path('course', CourseListView.as_view(), name='course_detail'),
    path('course/new', CourseCreateView.as_view(), name='course_new'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('course/<int:pk>/edit', CourseUpdateView.as_view(), name='course_edit'),
    path('course/<int:pk>/delete', CourseDeleteView.as_view(), name='course_delete'),
    path('approver', ApproverListView.as_view(), name='approver'),
    path('approver/<int:pk>', ApproverDetailView.as_view(), name='approver_detail'),
    path('approver/<int:pk>/edit', ApproverUpdateView.as_view(), name='approver_edit'),
    path('approver/new', ApproverCreateView.as_view(), name='approver_new'),
    path('approver/<int:pk>/delete', ApproverDeleteView.as_view(), name='approver_delete'),
]
