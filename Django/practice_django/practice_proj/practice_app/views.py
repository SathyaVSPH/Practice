#from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Member

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

def members(request):
    all_members = Member.objects.all().values()
    context = {
        'members_list' : all_members,
    }
    return render(request, 'Project2/members.html', context)

def details(request, id):
    member = Member.objects.get(id=id)
    context = {
        'member' : member,
    }
    template= loader.get_template('Project2/details.html')
    return HttpResponse(template.render(context, request))
