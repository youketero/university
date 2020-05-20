from django.test import TestCase, Client


# Create your tests here.
class UrlTest(TestCase):

    def test_home(self):
        c = Client()
        resp = c.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_article(self):
        c = Client()
        resp = c.get('/news/')
        self.assertEqual(resp.status_code, 200)

    def test_article_each(self):
        c = Client()
        resp = c.get('/article/ttt')
        self.assertEqual(resp.status_code,301)

    def test_anonce(self):
        c = Client()
        resp = c.get('/anonce/')
        self.assertEqual(resp.status_code, 200)

    def test_about(self):
        c = Client()
        resp = c.get('/info/')
        self.assertEqual(resp.status_code, 200)

    def test_contact(self):
        c = Client()
        resp = c.get('/contact/')
        self.assertEqual(resp.status_code, 200)

    def test_info_students(self):
        c = Client()
        resp = c.get('/info_for_students/')
        self.assertEqual(resp.status_code, 200)

    def test_info_students_each(self):
        c = Client()
        resp = c.get('/info_for_students_detailed/Enter%20title%20heresdf')
        self.assertEqual(resp.status_code, 301)

    def test_anonce_each(self):
        c = Client()
        resp = c.get('/anonce/4')
        self.assertEqual(resp.status_code, 301)