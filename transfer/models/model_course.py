'''
model_course.py
Chris Meehan
4/12/2020
Updated:
4/26/2020
'''
from django.db import models
from django.urls import reverse
from .model_school import School


class Course(models.Model):
    '''
    This course model, is build on the data models given.
    '''
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    subject_no = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])
