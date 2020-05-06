'''
model_major.py
Chris Meehan
4/12/2020
'''
from django.db import models
from django.urls import reverse


class Major(models.Model):
    '''
    This model is build on the given model for Majors.
    '''
    major_name = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.major_name

    def get_absolute_url(self):
        '''
        Returns the redirect for major detail page
        '''
        return reverse('major_detail', args=[str(self.id)])
