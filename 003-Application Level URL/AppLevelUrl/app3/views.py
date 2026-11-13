from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def btech_view(request):
    return HttpResponse('<h3>Welcome to btech students</h3>')

def mca_view(request):
    return HttpResponse('<h3>Welcome to mca students</h3>')

def mba_view(request):
    return HttpResponse('<h3>Welcome to mba students</h3>')

def mtech_view(request):
    return HttpResponse('<h3>Welcome to mtech students</h3>')
