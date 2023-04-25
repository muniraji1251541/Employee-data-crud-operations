from django.shortcuts import render,redirect
from django.contrib import messages
from employee.forms import *
from employee.models import *

# Create your views here.

def emp_form(request,id=0):
    if id==0:
        form=EmpForm()
        if request.method=='POST':
            form=EmpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Data inserted successfully')
                return redirect('emp_list')
            
    else:
        emp=Employee.objects.get(pk=id)
        form=EmpForm(instance=emp)
        if request.method=='POST':
            form=EmpForm(request.POST,instance=emp)
            if form.is_valid():
                form.save()
                messages.success(request,'Data updated successfully')
                return redirect('emp_list')

    return render(request,'emp_form.html',{'form':form})


def emp_list(request):
    data=Employee.objects.all()
    return render(request,'emp_list.html',{'data':data})

def emp_delete(request,id):
    emp=Employee.objects.get(pk=id)
    emp.delete()
    messages.success(request,'Data deleted successfully')
    return redirect('emp_list')