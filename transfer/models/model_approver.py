'''
model_approver.py
Chris Meehan
4/12/2020
'''
from django.db import models
from django.urls import reverse
# Create your models here.


class Approver(models.Model):
    '''
    Model for approver, based on data model given.
    '''

    approver_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.approver_name

    def get_absolute_url(self):
        return reverse('approver_detail', args=[str(self.id)])
