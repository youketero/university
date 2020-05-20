from django.contrib import admin

# Register your models here.
from structure.models import structure_staff, structure_person, stucture_cathed

admin.site.register(structure_staff)

class structure_person_fil(admin.ModelAdmin):
    list_display = ["name","last_name"]

    class Meta:
        model = structure_person

admin.site.register(structure_person,structure_person_fil)


class structure_cathed_fil(admin.ModelAdmin):
    list_display = ["cathed_name"]

    class Meta:
        model = stucture_cathed

admin.site.register(stucture_cathed, structure_cathed_fil)