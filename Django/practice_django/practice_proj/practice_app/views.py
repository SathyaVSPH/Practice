#from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from django.shortcuts import redirect

def greet(request):
    return HttpResponse('Hello, World!')

def redirect_to_welcome(request):
    return redirect('welcome/')

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def project1(request):
    template = loader.get_template('tables.html')
    return HttpResponse(template.render())