from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from photologue.models import Gallery

from entrance.models import entrance_specialization_way
from information_block.models import Partner, Articles, Info, future_conference_anonce
from structure.models import stucture_cathed


def home(request):
    articles = Articles.objects.order_by('id').reverse()[:8]
    foto_galery = Gallery.objects.all()
    partners = Partner.objects.all()
    future_conference_anonce_full = future_conference_anonce.objects.all()
    sub = entrance_specialization_way.objects.filter(education_level="Бакалавр")
    mag = entrance_specialization_way.objects.filter(education_level="Магістр")
    cathed = stucture_cathed.objects.all()
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, 'information_block/home.html', locals())


def contact(request):
    return render(request, "information_block/contact.html", locals())


def partneru(request):
    partner_each = Partner.objects.all()
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, 'information_block/partner.html', locals())

def news(request):
    articles = Articles.objects.order_by('id').reverse()
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.get_page(page)
    except PageNotAnInteger:
        contacts=paginator.get_page(1)
    except EmptyPage:
        contacts = paginator.get_page(paginator.num_pages)
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, "information_block/news.html", locals())

def show_articles(request, article_title):
    article = get_object_or_404(Articles, title=article_title)
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, 'information_block/article.html', locals())

def anonce1(request):
    future_conference_anonce_full = future_conference_anonce.objects.all()
    return render(request, 'information_block/anonce.html', locals())

def anonce_detail(request, anonce_id):
    anonce_details = get_object_or_404(future_conference_anonce, id=anonce_id)
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, 'information_block/anonce_detail.html', locals())



def info(request):
    all_article = Articles.objects.order_by("id").reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, "information_block/Information.html", locals())

def info_for_students(request):
    info_for_student = Info.objects.order_by('id').reverse()
    paginator = Paginator(info_for_student, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, "information_block/info_for_students.html", locals())


def info_detailed(request, info_title):
    info_for_student = get_object_or_404(Info, title=info_title)
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, "information_block/info_for_students_detail.html", locals())

class search(View):

    def get(self, request, *args, **kwargs):

        query = self.request.GET.get('q')
        if query is not None:
            query = self.request.GET.get('q')
            if query:
                articles = Articles.objects.filter(title=query)
                partners = Partner.objects.filter(name=query)
        return render(request, "information_block/search_results.html", locals())


def handler404(request, *args, **argv):
    response = render(request,'base/page404.html')
    response.status_code = 404
    return response