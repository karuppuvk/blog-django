#from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse("hello world you are in home")
    return render(request, 'home.html')
def about(request):
    #return HttpResponse("my About page. ")
    return render(request,'about.html')