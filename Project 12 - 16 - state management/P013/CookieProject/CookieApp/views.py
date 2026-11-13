from django.shortcuts import render
from django.http import HttpResponse

def page_count_view(request):
    if 'count' in request.COOKIES:
        count=int(request.COOKIES['count'])+1
    else:
        count=1
    resp=HttpResponse()
    resp.set_cookie('count',count,max_age=60*60)
    return resp


        