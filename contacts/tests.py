"""
contacts unit tests
functional tests are in ..
"""
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from contacts.views import home_page
from contacts.models import Organisation

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


class OrganisationModelTest(TestCase):
    """check our model of Organisations"""
    def test_saving_and_ordered_retrieving_orgs(self):
        """
        can we create organisations
        and get them back in the right order
        """
        first_org = Organisation()
        first_org.name = 'First Organisation Added'
        first_org.email = 'a@first.org'
        first_org.save()

        second_org = Organisation(
            name='Another Org', email='x@sec.org'
        )
        second_org.save()

        self.assertEqual(Organisation.objects.count(), 2)
        saved_orgs = Organisation.objects.all()
        first_ordered_org = saved_orgs[0]
        second_ordered_org = saved_orgs[1]
        self.assertEqual(first_ordered_org.name, 'Another Org')
        self.assertEqual(second_ordered_org.name, 'First Organisation Added')

    def test_string_representation(self):
        """
        does Organisation have a sensible
        string repr?
        """
        org = Organisation()
        org.name = 'First Organisation Added'
        org.save()
        saved_orgs = Organisation.objects.all()
        self.assertEqual(saved_orgs.count(), 1)
        self.assertEqual(str(saved_orgs[0]), org.name)

    def test_dafault_name_and_email(self):
        """are defaults what we expect?"""
        org = Organisation()
        org.save()
        saved_org = Organisation.objects.last()
        self.assertEqual(saved_org.name, '')
        self.assertEqual(saved_org.email, '')