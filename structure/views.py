from django.shortcuts import render, get_object_or_404

# Create your views here.
from structure.models import stucture_cathed, structure_person


def structure(request):
    cathed2 = stucture_cathed.objects.all()
    cathed_count = stucture_cathed.objects.count()
    return render(request, "structure/structure.html", locals())


def cathed_b(request, cathed_name):
    cathed_each = get_object_or_404(stucture_cathed, cathed_name=cathed_name)
    teacher1 = structure_person.objects.filter(cathed_id__cathed_name=cathed_name)
    return render(request, "structure/cathed.html", locals())

def teacher(request, teacher):
    teacher = get_object_or_404(structure_person, id=teacher)
    return render(request, "structure/teacher_info.html", locals())