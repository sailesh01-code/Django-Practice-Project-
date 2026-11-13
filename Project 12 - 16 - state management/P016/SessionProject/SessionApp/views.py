from django.shortcuts import render,HttpResponse

# Create your views here.
def create_session(request):
    request.session['name']='surendra'
    request.session['mark']=79
    request.session['course']='MTech'
    return HttpResponse('Session is set')

def get_session(request):
    name=request.session['name']
    mark=request.session['mark']
    items=request.session.items()
    keys=request.session.keys()  
    exp_date=request.session.get_expiry_date()
    exp_age=request.session.get_expiry_age()
    context={
        'name':name,
        'mark':mark,
        'items':items,
        'keys':keys,
        'exp_date':exp_date,
        'exp_age':exp_age,
    }
    return render(request,'SessionApp/get_session.html',context)

def delete_session(request):
    del request.session['mark']
    return HttpResponse('Session - mark deleted')

def page_count(request):
    count=request.session.get('count',0)
    newcount=count+1
    c=request.session['count']=newcount
    return HttpResponse(c)





