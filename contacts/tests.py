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

    def test_can_save_a_POST_request(self):
        """can home page save POST?"""
        response = self.client.post('/', data={'organisation_name': 'New Organisation'})
        self.assertIn('New Organisation', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
