from django.shortcuts import render
from django.http import HttpResponse

def puri_view(request):
    return HttpResponse('<h1>Welcome to jagannath dham</h1>')

def bbsr_view(request):
    return HttpResponse('<h1>Welcome to lingaraj</h1>')

def cuttack_view(request):
    return HttpResponse('<h1>Welcome to silver city</h1>')
