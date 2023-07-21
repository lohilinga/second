from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def srinu (request):
    return HttpResponse(' Srinu is a good Boy')
def karthik (request):
    return HttpResponse('<marquee><h1>Karthik is a innocent<h1/></marquee>')
