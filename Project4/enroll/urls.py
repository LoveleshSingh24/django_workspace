from django.urls import path
from . import views

urlpatterns = [
    path('',views.studentinfo),
    path('students/',views.studentinfo),
    path('registration/',views.showFormData)
]
