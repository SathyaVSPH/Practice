#from django.shortcuts import render
from .models import Book
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    books = Book.objects.all().values()
    template = loader.get_template('homepage.html')
    context = { 'books' : books}
    return HttpResponse(template.render(context, request))