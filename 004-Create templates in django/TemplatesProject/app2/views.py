from django.shortcuts import render  # type: ignore[import-not-found]

# Create your views here.
def puri_view(request):
    return render(request, 'app2/puri.html')

def bbsr_view(request):
    return render(request,'app2/bbsr.html')
