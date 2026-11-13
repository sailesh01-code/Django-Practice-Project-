from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish_view(request):
    return HttpResponse('<h1>Hello Students Good Evening</h1>')
