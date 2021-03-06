from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from businessapp.forms import EmployeeForm
from businessapp.models import Employee


def adddata(request):
	if request.method == 'GET':
		form = 	EmployeeForm(request.GET)
		if form.is_valid():
			form.save()
			return redirect('/getdata/')
	else:
		form = EmployeeForm()
	return render(request,'form.html',{'form':form})

def getdata(request):
	data = Employee.objects.all()
	return render(request,'show.html',{'data':data})
	
def delete(request,id):
	# return HttpResponse(id)
	data = Employee.objects.get(id=id)
	data.delete()
	return redirect('/getdata/')

def getdataforedit(request,id):

	data = Employee.objects.get(id=id)
	return render(request,'editdata.html',{'data':data})

def update(request,id):
	if request.method == "GET":
		emp = Employee.objects.get(id=id)
		form = EmployeeForm(request.GET,instance=emp)
		if form.is_valid():
			try:
				form.save()
				return redirect('/getdata')
			except:
				pass
	else:
		form = EmployeeForm()
	return render(request,"editdata.html",{'form':form})
    