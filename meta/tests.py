from django.test import TestCase
from django.urls import reverse_lazy

class MetaURLsTestCase(TestCase):
    def test_404(self):
        res = self.client.get('/dfhjjksjhkdsakjhs')
        self.assertEqual(res.status_code, 404)

        # check that our custom 404 page is shown
        self.assertIn(b'<meta charset="utf-8">\n  '
                      b'<title>Page Not Found</title>\n  '
                      b'<meta name="viewport" content="width=device-width, initial-scale=1">',
                      res.content)

    def test_home(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_home_name(self):
        res = self.client.get(reverse_lazy('meta-home-page'))
        self.assertEqual(res.status_code, 200)

    def test_restframework_login(self):
        res = self.client.get('api-auth/login/')
        self.assertEqual(res.status_code, 200)
