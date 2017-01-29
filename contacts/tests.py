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

    def test_home_page_template_used(self):
        """do we actualy get sense from `home_page` view"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
