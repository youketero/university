from django.shortcuts import render, get_object_or_404

# Create your views here.
from entrance.models import entrance_specialization_way


def vstup(request):
    sub_mag = entrance_specialization_way.objects.filter(education_level="Магістр")
    sub_bac = entrance_specialization_way.objects.filter(education_level="Бакалавр")
    return render(request, "entrance/vstup.html", locals())


def vstup_info(request, id, ed_form):
    map_code = {103:"Науки про Землю", 193:"Геодезія та землеустрій"}
    vs = get_object_or_404(entrance_specialization_way, code_id__specialization_id__specialization_name=id, education_level=ed_form)
    map = map_code.get(vs.code_id.specialization_code)
    sub1 = entrance_specialization_way.objects.filter(education_level="Бакалавр")
    return render(request, "entrance/vstup_info.html", locals())