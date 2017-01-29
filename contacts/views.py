"""
bulding out home page, contacts etc.etc.
"""
from django.shortcuts import render

from contacts.models import Organisation


def home_page(request):
    """no place like home"""
    org = Organisation()
    org.name = request.POST.get('organisation_name', '')
    org.save()
    return render(request, 'home.html', {
        'new_organisation_name': org.name,
    })
