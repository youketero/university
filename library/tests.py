from django.test import TestCase, Client

# Create your tests here.
class UrlTest(TestCase):
    def test_edu_plan(self):
        c = Client()
        resp = c.get('/library/')
        self.assertEqual(resp.status_code, 200)
