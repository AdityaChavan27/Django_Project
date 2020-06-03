from django import forms
from django.core import validators
from django.forms import ModelForm
from.models import login



# def check(value):
#     if not any(i.isupper() for i in value):
#         raise forms.ValidationError("Please enter 1 upper case letters.")
# def check1(value):
#      if not any(i.islower() for i in value ):
#          raise forms.ValidationError("Please enter 1 lower case letters.")
# def check2(value):
#      if not any(i.isnumeric() for i in value):
#         raise forms.ValidationError("Please enter 1 numeric value")
# def check3(value):
#     ss = ['$', '@', '#', '%']
#     count=0
#     for i in range(len(value)):
#         if(value[i] in ss):
#             count+=1
#     if(count<2):
#         raise forms.ValidationError("Please enter 2 Special Characters")
#
class loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'

#     name=forms.CharField(label="Enter your name ")
#     email=forms.EmailField(max_length=30)
#     verify_email=forms.EmailField(label="Repeat Email")
#     text=forms.CharField(widget=forms.Textarea)
#     password=forms.CharField(widget=forms.PasswordInput,validators=[check,check1,check2,check3])
#
#
#     def clean(self):
#         email = self.cleaned_data.get('email')
#         vemail = self.cleaned_data.get('verify_email')
#         if email !=vemail:
#             raise forms.ValidationError("Please provide the correct email address")









