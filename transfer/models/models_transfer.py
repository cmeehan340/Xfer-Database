from django.db import models
from django.urls import reverse
# Create your models here.


class School(models.Model):
    school_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.school_name

    def get_absolute_url(self):
        return reverse('school_name', args=[str(self.id)])


class Course(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    subject_no = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    sem_year_taken = models.CharField(max_length=8)
    expiration_date = models.DateField()
    approved_status = models.CharField(max_length=1)
    comment = models.CharField(max_length=150)
    # approver_id = models.ForeignKey(Approver, on_delete=models.CASCADE)


class MajorRequirment(models.Model):
    description = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.description
