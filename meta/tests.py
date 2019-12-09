from django.test import TestCase

class MetaTestCase(TestCase):
    def test_404(self):
        res = self.client.get('/dfhjjksjhkdsakjhs')
        self.assertEqual(res.status_code, 404)
        self.assertIn(b'<meta charset="utf-8">\n  '
                      b'<title>Page Not Found</title>\n  '
                      b'<meta name="viewport" content="width=device-width, initial-scale=1">',
                      res.content)

    def test_home(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 404)
