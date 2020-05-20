from django.shortcuts import render

# Create your views here.
from entrance.models import entrance_specialization_way


def edu_plans(request):
    sub = entrance_specialization_way.objects.all()
    return render(request, "learning/edu_plan.html", locals())


def education(request):
    return render(request, "learning/education.html", locals())

def science_learning(request):
    return render(request, "learning/science_learning.html", locals())


def phd_learning(request):
    return render(request, 'learning/phd_learning.html', locals())