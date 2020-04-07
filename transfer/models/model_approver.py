from django.db import models


class Aprover(models.Model):
    approver_id = models.CharField(max_length=30, blank=False)
    approver_name = models.CharField(max_length=30, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.approver_id
