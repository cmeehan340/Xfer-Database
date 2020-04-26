'''
model_course.py
Chris Meehan
4/12/2020
Updated:
4/26/2020
'''
from django.db import models
from .model_approver import Approver
from .model_school import School


class Course(models.Model):
    '''
    This course model, is build on the data models given.
    '''
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    subject_no = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.title
