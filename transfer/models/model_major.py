from django.db import models


class Major(models.Model):
    major_id = models.CharField(max_length=30, blank=False)
    major_name = models.CharField(max_length=30, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.major_id
