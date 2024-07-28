from django.contrib import admin
from enroll.models import Student
# Register your models here.

# #to represent the all the data in table we use studentAdmin class
# class StudentAdmin(admin.ModelAdmin):
#     list_display=('id','studid','studname','studemail','studpass','comment')
#     #list display takes tuple or list (id,)
# admin.site.register(Student,StudentAdmin);

#register model admin class using decorator 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','studid','studname','studemail','studpass','comment')
