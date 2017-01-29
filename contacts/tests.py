"""
contacts unit tests
functional tests are in ..
"""
from django.core.urlresolvers import resolve
from django.test import TestCase

from contacts.views import home_page


class HomePageTest(TestCase):
    """there's no place like..."""

    def test_root_url_returns_home_page_view(self):
        """can we load home page"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)
