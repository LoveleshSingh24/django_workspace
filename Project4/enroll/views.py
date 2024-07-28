from django.shortcuts import render
from enroll.models import Student
from . import forms

# Create your views here.

def studentinfo(request):
    stud=Student.objects.get(pk=2)# return the query set having data from data base
    print('myOutput :',stud);
    return render(request,'enroll/stu_info.html',{'stu':stud})


def showFormData(request):
    fn=forms.StudentRgistration(auto_id=True) #id will get same name as field name,label value also changes with it
    #auto id=string not follow by any %s will be consider true 
    #auto id=False->label tag,id attribute is not available
    #by default is is 'id_fieldName'
    return render(request,'enroll/userregistration.html',{'form':fn})
