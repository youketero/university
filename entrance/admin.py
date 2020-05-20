from django.contrib import admin

# Register your models here.
from entrance.models import entrance_code, entrance_subject, entrance_specialization, entrance_specialization_way

admin.site.register(entrance_code)
admin.site.register(entrance_subject)
admin.site.register(entrance_specialization)
admin.site.register(entrance_specialization_way)