from django.test import TestCase, Client


# Create your tests here.
from photologue.models import Gallery

from entrance.models import entrance_specialization, entrance_subject, entrance_code, entrance_specialization_way


class UrlTest(TestCase):

    def test_vstup(self):
        c = Client()
        resp = c.get('/vstup')
        self.assertEqual(resp.status_code, 200)

    def test_vstup_each(self):
        c = Client()
        resp = c.get('/vstup/Геологія')
        self.assertEqual(resp.status_code, 301)

class ModelTest(TestCase):

    def create_whatever(self, subject_name="only a test", weigth_coef=0.1, min_grade= 120):
        return entrance_subject.objects.create(
            subject_name=subject_name, weigth_coef=weigth_coef, min_grade=min_grade)

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, entrance_subject))
        self.assertEqual(w.__str__(), str(w.subject_name))

