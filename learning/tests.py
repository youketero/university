from django.test import TestCase, Client


# Create your tests here.
class UrlTest(TestCase):

    def test_edu_plan(self):
        c = Client()
        resp = c.get('/edu_plan/')
        self.assertEqual(resp.status_code, 200)

    def test_education(self):
        c = Client()
        resp = c.get('/education/')
        self.assertEqual(resp.status_code, 200)

    def test_science_learning(self):
        c = Client()
        resp = c.get('/science_learning/')
        self.assertEqual(resp.status_code, 200)

    def test_phd_learning(self):
        c = Client()
        resp = c.get('/phd_learning/')
        self.assertEqual(resp.status_code, 200)

