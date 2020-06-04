from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from.models import login
def home(request):
    return render(request,"myapp\home.html")
def aboutus(request):
    return HttpResponse("This web page is created in Django")

def contact(request):
    return HttpResponse("My official email-id is: aac84@njit.edu")

def home1(request):
    return render(request,"myapp\home1.html")

# def form_view(request):
#     if(request.method=="POST"):
#         form=forms.loginform(request.POST)
#         if form.is_valid():
#             print('validation worked')
#             print("name : " + form.cleaned_data["name"])
#             print("Email : " + form.cleaned_data["email"])
#             print("Text: " + form.cleaned_data["text"])
#     else:
#
#         form=forms.loginform()
#     return render (request,'myapp\index.html',{'form':form})


def create(request):
    if request.method=="POST":
        form=forms.loginform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form=forms.loginform()


    return render(request,'myapp\index.html',{'form':form})

def success(request):
    return render(request,'myapp/success.html')


def show(request):
    logins=login.objects.all()
    return render(request,"myapp/show.html",{'logins':logins})


# Create your views here.
