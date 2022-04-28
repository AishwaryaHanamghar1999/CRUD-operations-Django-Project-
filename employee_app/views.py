from django.shortcuts import render,redirect
from employee_app.models import emp_info
from .forms import emp_form
from .models import emp_info

# Create your views here.
def show(request):
    employee=emp_info.objects.all()
    return render(request,'show.html',{'emp':employee})

def add(request):
    if(request.method=='POST'):
        fm=emp_form(request.POST)
        if fm.is_valid():
            try:
                fm.save()
                return redirect('/show')
            except:
                pass
    else:
        fm=emp_form()
    return render(request,'add.html',{'form':fm})

def edit(request,id):
    employee=emp_info.objects.get(id=id)
    return render(request,'update.html',{'employee':employee})

def update(request,id):
    emp=emp_info.objects.get(id=id)
    form=emp_form(request.POST,instance=emp)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'update.html',{'employee':emp})

def delete(request,id):
    emp=emp_info.objects.get(id=id)
    emp.delete()
    return redirect('/show')
    
        