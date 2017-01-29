"""
bulding out home page, contacts etc.etc.
"""
from django.shortcuts import render

from contacts.models import Organisation


def home_page(request):
    """no place like home"""
    return render(request, 'organisations_list.html')

def create_organisation(request):
    if request.method == 'POST':
        org = Organisation()
        org.name = request.POST.get('organisation_name', '')
        org.email = request.POST.get('organisation_email', '')
        org.save()
        print('BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD')
        from django.http import HttpResponse
        return HttpResponse(request.POST['organisation_name'])
    return render(request, 'new_organisation.html')
