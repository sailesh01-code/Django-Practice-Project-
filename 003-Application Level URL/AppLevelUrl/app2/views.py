from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def morning_view(request):
    return HttpResponse('<h2>Good Morning Students </h2>')

def evening_view(request):
    return HttpResponse('<h2>Good Evening Students </h2>')
