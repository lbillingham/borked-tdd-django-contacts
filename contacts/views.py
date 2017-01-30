"""
bulding out home page, contacts etc.etc.
"""
# from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView


from contacts.models import Organisation


class OrganisationListView(ListView):

    model = Organisation
    template_name = 'organisation_list.html'


# class CreateOrganisationView(CreateView):
    # model = Organisation
    # template_name = 'new_organisation.html'
    # fields = ('name', 'email', )
#
    # def get_success_url(self):
        # return reverse('organisations-list')
#