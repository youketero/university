from django.db import models

# Create your models here.
from structure.models import stucture_cathed


class subject_edu(models.Model):
    subj_name = models.TextField(default="enter name of subject here")
    code = models.TextField(default="OK 1")
    count_credits = models.IntegerField(default="2")
    form_control = models.TextField(default="Іспит")
    cathed_specialization = models.ForeignKey(stucture_cathed, default=1, on_delete=models.CASCADE)


class edu_plan(models.Model):
    choise_cource = ((1, '1'), (2, '2'), (3, '3'), (4, "4"))
    edu_plan_doc = models.FileField(upload_to="web/static/docs")
    cource = models.IntegerField(default=1, choices=choise_cource)

    def __str__(self):
        return "%s" % (self.edu_plan_doc)


class edu_prog(models.Model):
    specialization_id = models.ForeignKey(edu_plan, default=1, on_delete=models.CASCADE)
    subject_edu_id = models.ForeignKey(subject_edu, default=1, on_delete=models.CASCADE)
    language = models.TextField(default="Українська")
    credit_sum = models.IntegerField(default=240)

    def __str__(self):
        return "%s" % (self.specialization_id)
