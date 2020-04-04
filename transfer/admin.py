from django.contrib import admin
from .models.models_transfer import School, Course

# Register your models here.
admin.site.register(School)
admin.site.register(Course)
