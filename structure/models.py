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
    foto = models.ImageField(upload_to='structure/cathed')
    foto_logo = models.ImageField(upload_to='structure/cathed', default="#")
    history = models.TextField(default="empty")
    description = models.TextField(default="empty")
    education  = models.TextField(default="empty")
    science_edu = models.TextField(default="empty")
    email = models.TextField(default="http")
    number = models.CharField(max_length=25)
    address = models.TextField(default="Kyiv")

    def __str__(self):
        return "%s" % self.cathed_name


class structure_person(models.Model):
    name = models.TextField(default='name')
    last_name = models.TextField(default="sername")
    middle_name = models.TextField(default="middlename")
    foto = models.ImageField(upload_to='structure_person', default="#")
    short_history = models.TextField(default='history')
    phone_number = models.CharField(max_length=25)
    link_to_facebook = models.CharField(max_length=100, default="#")
    link_to_twitter = models.CharField(max_length=100, default="#")
    email = models.CharField(max_length=50, default="email@gmail.com")
    monography = models.TextField(default="monography")
    step = models.TextField(default="doctor")
    cathed_id = models.ForeignKey(stucture_cathed, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(structure_staff, default=1, on_delete=models.CASCADE)
    lab_staff = models.BooleanField(default=1)

    def __unicode__(self):
        return "%s %s" % (self.name, self.last_name)

    def short_text(self):
        if len(self.short_history) > 100:
            return self.short_history[:100] + '...'
        else:
            return self.short_history


class structure_laboratory(models.Model):
    lab_name = models.TextField(max_length=50)
    lab_name_rus = models.TextField(max_length=100, default="write")
    description = models.TextField(default="enter desciption here")
    history = models.TextField()
    foto = models.ImageField(upload_to='structure/laboratory')
    number = models.CharField(max_length=25)
    email = models.TextField(default="http")
    address = models.TextField(default="Kyiv")
    cathed_id = models.ForeignKey(stucture_cathed, default=1, on_delete=models.CASCADE)
