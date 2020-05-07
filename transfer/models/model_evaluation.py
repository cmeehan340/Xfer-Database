'''
model_evaluation.py
Chris Meehan
4/26/2020
'''

from django.db import models
from .model_approver import Approver
from .model_requirement import MajorRequirement
from .model_course import Course


class TransferEvaluation(models.Model):
    '''
    This is the Transfer Evaluation model, built based on the provided data
    model
    '''
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    major_req_id = models.ForeignKey(MajorRequirement, on_delete=models.CASCADE)
    sem_year_taken = models.CharField(max_length=50, blank=True, null=True)
    expiration_date = models.DateField()
    approved_status = models.CharField(max_length=10, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    approver_id = models.ForeignKey(Approver, on_delete=models.CASCADE)


    def get_absolute_url(self):
        '''
        Returns the redirect for major detail page
        '''
        return reverse('eval_detail', args=[str(self.id)])
