from django.db import models


class Approver(models.Model):
    approver_name = models.CharField(max_length=30, blank=False, unique=True)


    def __str__(self):
        return self.approver_name
