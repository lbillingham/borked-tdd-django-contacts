"""
bulding out home page, contacts etc.etc.
"""
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    """no place like home"""
    return render(request, 'home.html', {
        'new_organisation_name': request.POST.get('organisation_name', ''),
    })
