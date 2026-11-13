from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_cookie_view(request):
    resp=HttpResponse('Cookie is set')
    resp.set_cookie('mark','75')
    return resp





def get_cookie_view(request):
    name = request.COOKIES.get('name', 'Not set')
    mark = request.COOKIES.get('mark', 'Not set')
    return HttpResponse(f'Cookie Name is {name} Mark is {mark}')

def delete_cookie_view(request):
    resp=HttpResponse('Cookie deleted')
    resp.delete_cookie('name')
    return resp