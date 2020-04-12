'''
model_majorreq.py
Chris Meehan
4/12/2020
'''
from django.db import models
# Create your models here.


class MajorRequirment(models.Model):
    '''
    This model is build for the Major Requirment based on the given data.
    '''
    description = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.description
