from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def home(request):
    return render(request,"myapp\home.html")
def aboutus(request):
    return HttpResponse("This web page is created in Django")

def contact(request):
    return HttpResponse("My official email-id is: aac84@njit.edu")

def home1(request):
    return render(request,"myapp\home1.html")

def form_view(request):
    if(request.method=="POST"):
        form=forms.loginform(request.POST)
        if form.is_valid():
            print('validation worked')
            print("name : " + form.cleaned_data["name"])
            print("Email : " + form.cleaned_data["email"])
            print("Text: " + form.cleaned_data["text"])
    form=forms.loginform
    return render (request,'myapp\index.html',{'form':form})



# Create your views here.
