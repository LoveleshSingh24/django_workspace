from django import forms

class StudentRgistration(forms.Form):
    name=forms.CharField(initial='lovelesh',help_text="this field contain 30 char") #no data
    email=forms.EmailField()
