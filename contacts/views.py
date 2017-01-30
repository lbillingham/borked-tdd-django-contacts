"""
bulding out home page, contacts etc.etc.
"""
from django.shortcuts import redirect, render

from contacts.models import Organisation


def home_page(request):
    """no place like home"""
    return render(request, 'organisations_list.html')

def create_organisation(request):
    if request.method == 'POST':
        print('CreateCreate\n{}\nCreateCreate'.format(request))
        Organisation.objects.create(
            name=request.POST.get('organisation_name', ''),
            email=request.POST.get('organisation_email', '')
        )
        return redirect('/')
    else:
        return render(request, 'new_organisation.html')
