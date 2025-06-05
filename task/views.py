from django.shortcuts import render,redirect
from . models import Details
from django.http import HttpResponse
# Create your views here.
def task(request):
    if request.method=="POST":
        tname_var=request.POST['tname']
        tdesc_var=request.POST['tdesc']
        tdate_var=request.POST['tdate']
    
        Details.objects.create(
                      t_name=tname_var,
                      t_desc=tdesc_var,
                      t_date=tdate_var,  
    )
        return redirect('task')
    data=Details.objects.all().order_by('-id')
    context={
        'datas':data,
    }
    return render (request,'home.html',context)
def edit(request,id):
    try:
        data=Details.objects.get(id=id)
    except:
        return HttpResponse("data not found")
    if request.method=="POST":
        data.t_name=request.POST['tname']
        data.t_desc=request.POST['tdesc']
        data.t_date=request.POST['tdate']
        data.save()
        return redirect('task')
    return render(request,'edit.html')
def delete(request,id):
    try:
        data=Details.objects.get(id=id)
    except:
        return HttpResponse("data not found")
    data.delete()
    return redirect ('task')
