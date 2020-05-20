from django.test import TestCase, Client


# Create your tests here.
class UrlTest(TestCase):
    def test_structure(self):
        c = Client()
        resp = c.get('/structure/')
        self.assertEqual(resp.status_code, 200)

    def test_structure_each(self):
        c = Client()
        resp = c.get('/structure/sfasfa')
        self.assertEqual(resp.status_code, 301)

    def test_teacher(self):
        c = Client()
        resp = c.get('/teacher/1')
        self.assertEqual(resp.status_code, 301)

