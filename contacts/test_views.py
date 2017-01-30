"""
unit tests for views
don't need to do much after switch to class based generic views
functional tests are in ..
"""
from django.core.urlresolvers import reverse
from django.test import TestCase

from contacts.models import Organisation

_ENCODING = 'utf8'

class HomePageTest(TestCase):
    """
    Test Home page resolves to showing organisations list
    note uses `django.test.TestCase.client`
    if tests run too slow `RequestFactory` may help
    """

    def test_home_page_uses_organisation_list_template(self):
        """do we load the organisations list template into home_page"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'organisation_list.html')

    def test_home_page_lists_organisations(self):
        """do we list organisations on the home page, or nowt if no orgs?"""
        response = self.client.get('/')
        # no organisations yet , list should be empty
        self.assertEquals(list(response.context['object_list']), [])

        # create an Organisation, there should be a thing in the list
        Organisation.objects.create(name='1st name', email='first@example.com')
        response = self.client.get('/')
        self.assertEquals(response.context['object_list'].count(), 1)


class CreateOrganisationTest(TestCase):
    """can we create a new organisation?"""
    def test_new_organisation_template_used(self):
        response = self.client.get(reverse('organisations-new'))
        self.assertTemplateUsed(response, 'edit_organisation.html')

    def test_POST_request_returns_success(self):
        response = self.client.post(
            reverse('organisations-new'),
            data={'organisation_name': 'New Organisation',
                  'organisation_email': 'a@example.com'}
        )
        self.assertEqual(response.status_code, 200)
