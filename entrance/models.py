from django.db import models

# Create your models here.
from learning.models import edu_plan


class entrance_specialization(models.Model):
    specialization_name = models.TextField(default="enter specialization here")
    foto = models.ImageField(upload_to='entrance/specialization', default="#")

    def __str__(self):
        return "%s" % (self.specialization_name)


class entrance_subject(models.Model):
    subject_name = models.TextField(default="enter subject here")
    weigth_coef = models.FloatField(default=0.1)
    min_grade = models.IntegerField(default=1)

    def __str__(self):
        return "%s" % (self.subject_name)


class entrance_code(models.Model):
    specialization_code = models.IntegerField(default=103)
    specialization_id = models.ForeignKey(entrance_specialization, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "%s,%s" % (self.specialization_code, self.specialization_id)

class entrance_specialization_way(models.Model):
    choise_field = (('Бакалавр', 'Бакалавр'), ('Магістр', 'Магістр'), ('Молодший спеціаліст', 'Молодший спеціаліст'))
    code_id = models.ForeignKey(entrance_code, on_delete=models.CASCADE)
    subject_id = models.ManyToManyField(entrance_subject)
    edu_plan_id = models.ManyToManyField(edu_plan)
    form_education = models.TextField(choices=choise_field, max_length=1000,
                                      default="enter your form of education here")
    education_level = models.TextField(max_length=1000, default="enter your education level here")
    license = models.IntegerField(default=1)
    payment = models.IntegerField(default=1)
    duration_of_study = models.IntegerField(default=1)
    short_description = models.TextField(max_length=100000, default="Enter description here")

    def __str__(self):
        return "%s,%s" % (self.code_id, self.license)