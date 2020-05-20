from django.contrib import admin

# Register your models here.
from learning.models import edu_plan, edu_prog

admin.site.register(edu_plan)
admin.site.register(edu_prog)