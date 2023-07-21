from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def lohi (request):
    return HttpResponse ('<h1><marquee>hello World</marquee></h1>')
def linga (request):
    return HttpResponse ('<h1><marquee>My Name is lohidasu</marquee></h1>')
