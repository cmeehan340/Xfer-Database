from django.contrib import admin
from .models.model_major import Major
from .models.model_school import School
from .models.model_course import Course
from .models.model_requirement import MajorRequirement
from .models.model_approver import Approver
# Register your models here.


admin.site.register(School)
admin.site.register(Course)
admin.site.register(MajorRequirement)
admin.site.register(Approver)
admin.site.register(Major)
