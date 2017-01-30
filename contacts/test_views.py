"""
contacts unit tests
functional tests are in ..
"""
from django.test import TestCase, RequestFactory


from contacts.models import Organisation
# from contacts.views import CreateOrganisationView

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




# class CreateOrganisationTest(TestCase):
#     """can we create a new organisation?"""
#     def test_saving_a_POST_request(self):
#         self.assertEqual(Organisation.objects.count(), 0)
#         response = self.client.post(
#             '/new-organisation',
#             data={'organisation_name': 'New Organisation',
#                   'organisation_email': 'a@example.com'}
#         )
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(Organisation.objects.count(), 1)
#         new_org = Organisation.objects.first()
#         self.assertEqual(new_org.name, 'New Organisation')
#         self.assertEqual(new_org.eamil, 'a@example.com')


#     def test_redirects_after_POST(self):
#         response = self.client.post(
#             '/new-organisation',
#             data={'organisation_name': 'New Organisation',
#                   'organisation_email': 'a@example.com'}
#         )
#         new_list = Organisation.objects.first()
#         self.assertRedirects(response, '/') # /lists/%d/' % (new_list.id,))




    # def setUp(self):
    #     self.create_org_url = '/new-organisation'
    #     self. default_data = {'organisation_name': 'New Organisation',
    #                           'organisation_email': 'a@example.com'}
    #     self.factory = RequestFactory()

    # def test_new_organisation_template_used(self):
    #     """with a GET/visit, do we render template?"""
    #     response = self.client.get(self.create_org_url)
    #     self.assertTemplateUsed(response, 'new_organisation.html')



    # def test_can_save_a_POST_request(self):
    #     """can new organisation page process POST to Model"""
    #     print('testing save POST')
    #     request = self.factory.get(self.create_org_url)
    #     response = CreateOrganisationView.as_view()(request)
    #     self.assertEquals(list(response.context['object_list']), [])
    #     response = self.client.post(self.create_org_url,
    #                                 data=self.default_data)
    #     request = self.factory.post(self.create_org_url, data=self.default_data)
    #     response = CreateOrganisationView.as_view()(request)
    #     # self.assertEqual(Organisation.objects.count(), 1)
    #     # new_org = Organisation.objects.first()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.template_name[0], 'new_organisation.html')
    #     print('###############\n{}\n#############'.format(response.context_data))
    #     self.assertEqual(response.context_data['name'], 'New Organisation')
    #     self.assertEqual(response.context_data['email'], 'a@example.com')
    #     # self.assertEqual(new_org.name, 'New Organisation')
    #     # self.assertEqual(new_org.email, 'a@example.com')

    # def test_redirects_after_POST(self):
    #     """after creating an organisation, we should redirect to home"""
    #     print('testing POST redirect')
    #     response = self.client.post(self.create_org_url,
    #                                 data=self.default_data)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response['location'], '/')
