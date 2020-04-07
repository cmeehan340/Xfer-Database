from django.db import models


class Major(models.Model):
    major_name = models.CharField(max_length=30, blank=False, unique=True)

    def __str__(self):
        return self.major_name
