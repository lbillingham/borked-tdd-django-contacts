"""
bulding out home page, contacts etc.etc.
"""
# from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    """no place like home"""
    return HttpResponse('<html><title>Contacts</title><html>')
