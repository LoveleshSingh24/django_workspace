from django.db import models

# Create your models here.

#we created the model calss sql statement in python
#we (manage.py makemigrations) create the python fine having all the changes 
#command (manage.py show migration) to show migration
#to implement the migrationn on the app we use command (pyhton manage.py migrate) this execute the query to make  schema and indsert delete
#to again implemant the chage we have to make all two command to (manage.py makemigrations) and (pyhton manage.py migrate) to execute the query
class Student(models.Model):
    studid=models.IntegerField()
    studname=models.CharField(max_length=70)
    studemail=models.EmailField(max_length=70)
    studpass=models.CharField(max_length=70)
    #adding column 
    comment = models.CharField(max_length=40,default='not available')

    #it must alway return string to display name of the field
    def __str__(self):
        return str(self.studid)


