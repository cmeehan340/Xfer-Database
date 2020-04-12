'''
model_course.py
Chris Meehan
4/12/2020
'''
from django.db import models
from .model_approver import Approver
from .model_school import School


class Course(models.Model):
    '''
    This course model, is build on the data models given.
    '''
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    subject_no = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    sem_year_taken = models.CharField(max_length=8)
    expiration_date = models.DateField()
    approved_status = models.CharField(max_length=1)
    comment = models.CharField(max_length=150)
    approver_id = models.ForeignKey(Approver, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
