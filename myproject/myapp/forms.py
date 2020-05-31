from django import forms

class loginform(forms.Form):
    name=forms.CharField(label="Enter your name ")
    email=forms.EmailField(max_length=30)
    text=forms.CharField(widget=forms.Textarea)
