from django.urls import path

from .views.views import (
        SchoolListView,
        HomeListView,
        MajorListView,
        CourseListView
    )

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('school', SchoolListView.as_view(), name='school_detail'),
    path('major', MajorListView.as_view(), name='major_detail'),
    path('course', CourseListView.as_view(), name='course_detail'),
]
