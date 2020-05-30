from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"myapp\home.html")
def aboutus(request):
    return HttpResponse("This web page is created in Django")

def contact(request):
    return HttpResponse("My official email-id is: aac84@njit.edu")

def home1(request):
    return render(request,"myapp\home1.html")



# Create your views here.
