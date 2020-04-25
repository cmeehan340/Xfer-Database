from django.urls import path
from .views.home_view import HomeListView
from .views.course_view import (CourseListView,
                                CourseCreateView,
                                CourseDeleteView,
                                CourseUpdateView,
                                CourseDetailView)
from .views.major_view import (MajorListView,
                             MajorDetailView,
                             MajorCreateView,
                             MajorDeleteView,
                             MajorUpdateView)
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
from .views.requirement_view import  (RequirementListView,
                            RequirementCreateView,
                            RequirementDetailView,
                            RequirementDeleteView,
                            RequirementUpdateView)
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('schools', SchoolListView.as_view(), name='school_home'),
    path('schools/<int:pk>', SchoolDetailView.as_view(), name='school_detail'),
    path('schools-new', SchoolCreateView.as_view(), name='school_new'),
    path('schools-update/<int:pk>', SchoolUpdateView.as_view(), name='school_edit'),
    path('schools-delete/<int:pk>', SchoolDeleteView.as_view(), name='school_delete'),

    path('majors', MajorListView.as_view(), name='major_home'),
    path('majors/<int:pk>', MajorDetailView.as_view(), name='major_detail'),
    path('majors-new', MajorCreateView.as_view(), name='major_new'),
    path('majors-edit/<int:pk>', MajorUpdateView.as_view(), name='major_edit'),
    path('majors-delete/<int:pk>', MajorDeleteView.as_view(), name='major_delete'),

    path('courses', CourseListView.as_view(), name='course_home'),
    path('courses-new', CourseCreateView.as_view(), name='course_new'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('courses-edit/<int:pk>', CourseUpdateView.as_view(), name='course_edit'),
    path('courses-delete/<int:pk>', CourseDeleteView.as_view(), name='course_delete'),

    path('approvers', ApproverListView.as_view(), name='approver'),
    path('approvers/<int:pk>', ApproverDetailView.as_view(), name='approver_detail'),
    path('approvers-edit/<int:pk>', ApproverUpdateView.as_view(), name='approver_edit'),
    path('approvers-new', ApproverCreateView.as_view(), name='approver_new'),
    path('approvers-delete/<int:pk>', ApproverDeleteView.as_view(), name='approver_delete'),

    path('requirements', RequirementListView.as_view(), name='requirement_home'),
    path('requirements/<int:pk>', RequirementDetailView.as_view(), name='requirement_detail'),
    path('requirements-new', RequirementCreateView.as_view(), name='requirement_new'),
    path('requirements-edit/<int:pk>', RequirementUpdateView.as_view(), name='requirement_edit'),
    path('requirements-delete/<int:pk>', RequirementDeleteView.as_view(), name='requirement_delete'),
]
