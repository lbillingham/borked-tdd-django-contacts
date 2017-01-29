"""
bulding out home page, contacts etc.etc.
"""
from django.shortcuts import render

def home_page(request):
    """no place like home"""
    return render(request, 'home.html')
