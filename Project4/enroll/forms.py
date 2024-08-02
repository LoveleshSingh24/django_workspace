from django import forms

class StudentRgistration(forms.Form):
    name=forms.CharField() #no data
    email=forms.EmailField()
