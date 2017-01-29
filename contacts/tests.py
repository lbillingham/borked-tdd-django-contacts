"""
contacts unit tests
functional tests are in ..
"""
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from contacts.views import home_page

_ENCODING = 'utf8'

class HomePageTest(TestCase):
    """for a 1st test, there's no place like..."""

    def test_root_url_returns_home_page_view(self):
        """can we load home page"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """do we actualy get sense from `home_page` view"""
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode(_ENCODING)
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Contacts</title>', html)
        self.assertTrue(html.endswith('<html>'))
