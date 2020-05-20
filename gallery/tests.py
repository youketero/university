from django.test import TestCase, Client


# Create your tests here.
class UrlTest(TestCase):

    def test_gallery(self):
        c = Client()
        resp = c.get('/galery/')
        self.assertEqual(resp.status_code, 200)

    def test_gallery_each(self):
        c = Client()
        resp = c.get('/galery/keki')
        self.assertEqual(resp.status_code, 301)