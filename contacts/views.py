"""
bulding out home page, contacts etc.etc.
"""
# from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, UpdateView


from contacts.models import Organisation


class OrganisationListView(ListView):

    model = Organisation
    template_name = 'organisation_list.html'


class CreateOrganisationView(CreateView):

    model = Organisation
    template_name = 'edit_organisation.html'
    fields = ('name', 'email', )

    def get_success_url(self):
        return reverse('organisations-list')

    def get_context_data(self, **kwargs):
        context = super(CreateOrganisationView, self).get_context_data(**kwargs)
        context['action'] = reverse('organisations-new')
        return context

class UpdateOrganisationView(UpdateView):

    model = Organisation
    template_name = 'edit_organisation.html'
    fields = ('name', 'email', )

    def get_success_url(self):
        return reverse('organisations-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateOrganisationView, self).get_context_data(**kwargs)
        context['action'] = reverse('organisations-edit',
                                    kwargs={'pk': self.get_object().id})
        return context
