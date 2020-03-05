from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student(request):
    return HttpResponse('we are student')
    
def teacher(request):
    return HttpResponse('we are teacher')
def home_page_view(request):
    return render(request,'schoolapp/form.html')    
