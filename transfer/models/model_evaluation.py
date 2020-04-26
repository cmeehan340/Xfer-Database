'''
model_evaluation.py
Chris Meehan
4/26/2020
'''

from django.db import models
from .model_approver import Approver
from .model_requirment import MajorRequirment
from .model_course import Course


class TransferEvaluation(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    major_req_id =  models.ForeignKey(MajorRequirment, on_delete=models.CASCADE)
    sem_year_taken = models.CharField(max_length=8)
    expiration_date = models.DateField()
    approved_status = models.CharField(max_length=1)
    comment = models.CharField(max_length=150)
    approver_id = models.ForeignKey(Approver, on_delete=models.CASCADE)
