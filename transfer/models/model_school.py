'''
model_school.py
Chris Meehan
4/12/2020
'''
from django.db import models
from django.urls import reverse

class School(models.Model):
    '''
    This is a school model built from the data model.
    '''
    school_name = models.CharField(max_length=200)
    state_name = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name

    def get_absolute_url(self):
        '''
        Returns the url for school_name
        '''
        return reverse('school_detail', args=[str(self.id)])
