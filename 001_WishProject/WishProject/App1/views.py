from django.http import HttpResponse  # type: ignore[reportMissingModuleSource]

# Create your views here.
def wish_view(request):
    return HttpResponse('<h1>Welcome to the world of Django</h1>')
