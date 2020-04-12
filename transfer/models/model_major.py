'''
model_major.py
Chris Meehan
4/12/2020
'''
from django.db import models


class Major(models.Model):
    '''
    This model is build on the given model for Majors.
    '''
    major_name = models.CharField(max_length=30, blank=False, unique=True)

    def __str__(self):
        return self.major_name
