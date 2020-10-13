from django.contrib import admin

# Register your models here.
from learning.models import edu_plan, edu_prog, subject_edu

admin.site.register(edu_plan)
admin.site.register(edu_prog)
admin.site.register(subject_edu)