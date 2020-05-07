'''
model_requirment.py
Chris Meehan
4/21/2020
'''
from django.db import models
from django.urls import reverse
from .model_major import Major
# Create your models here.


class MajorRequirement(models.Model):
    '''
    This model is build for the Major Requirment based on the given data.
    '''
    description = models.CharField(max_length=200, blank=True, null=True)
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('requirement_detail', args=[str(self.id)])

    def __str__(self):
        return str(self.id)
