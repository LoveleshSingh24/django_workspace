from django.shortcuts import render
from enroll.models import Student
from . import forms

# Create your views here.

def studentinfo(request):
    stud=Student.objects.get(pk=2)# return the query set having data from data base
    print('myOutput :',stud);
    return render(request,'enroll/stu_info.html',{'stu':stud})


def showFormData(request):
    fn=forms.StudentRgistration(auto_id=True,label_suffix=' ',initial ={'name':'Sonam','email':'abc@gmail.com'})
    #name , email above are fied name initial is used to dynamical initalize field input value

    #order th field
    fn.order_fields(field_order=['email','name','first_name'])# by defult it is set to none and takes list with order field you want
    return render(request,'enroll/userregistration.html',{'form':fn})
