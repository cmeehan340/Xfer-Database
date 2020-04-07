from django.contrib import admin
from .models.models_transfer import School, Course, MajorRequirment
from .models.model_approver import Approver
from .models.model_major import Major

# Register your models here.
admin.site.register(School)
admin.site.register(Course)
admin.site.register(MajorRequirment)
admin.site.register(Approver)
admin.site.register(Major)
