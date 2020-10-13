from django.shortcuts import render, get_object_or_404

# Create your views here.
from entrance.models import entrance_specialization_way


def vstup(request):
    sub_mag = entrance_specialization_way.objects.filter(form_education="Магістр")
    sub_bac = entrance_specialization_way.objects.filter(form_education="Бакалавр")
    return render(request, "entrance/vstup.html", locals())


def vstup_info(request, id):
    vs = get_object_or_404(entrance_specialization_way, code_id__specialization_id__specialization_name=id)
    sub1 = entrance_specialization_way.objects.filter(form_education="Бакалавр")
    return render(request, "entrance/vstup_info.html", locals())