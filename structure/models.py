from django.contrib.auth.models import Permission
from django.db import models

# Create your models here.
class structure_staff(models.Model):
    staff_name = models.TextField(default="enter staff here")
    permission_id = models.ForeignKey(Permission, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.staff_name)


class stucture_cathed(models.Model):
    cathed_name = models.TextField(max_length=50)
    cathed_name_rus = models.TextField(max_length=100, default="write")
    history = models.TextField()
    foto = models.ImageField(upload_to='information_block/static/img')
    number = models.CharField(max_length=25)
    description = models.TextField(default="enter desciption here")
    email = models.TextField(default="http")

    def __str__(self):
        return "%s" % self.cathed_name


class structure_person(models.Model):
    name = models.TextField(default='name')
    last_name = models.TextField(default="sername")
    foto = models.ImageField(upload_to='information_block/static/img', default="#")
    short_history = models.TextField(default='history')
    cathed_id = models.ForeignKey(stucture_cathed, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(structure_staff, default=1, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=25)
    monography = models.TextField(default="monography")
    step = models.TextField(default="doctor")

    def __unicode__(self):
        return "%s %s" % (self.name, self.last_name)

    def short_text(self):
        if len(self.short_history) > 100:
            return self.short_history[:100] + '...'
        else:
            return self.short_history

