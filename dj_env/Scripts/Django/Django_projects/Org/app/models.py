from django.db import models

# Create your models here.
class Dept(models.Model):
    Dept_No = models.IntegerField(primary_key=True)
    DName = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)

class Emp(models.Model):
    Emp_No = models.IntegerField()
    EName = models.CharField(max_length=100)
    Job = models.CharField(max_length=100)
    Mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null = True, blank = True)
    Hire_date = models.DateField(null=True, blank=True) # default null = False, auto_now = True for current date(date of creation of object) and auto_now_add = True for date of model creation
    Sal = models.DecimalField(max_digits=6, decimal_places=2) # no null vals
    Comm = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True)
    Dept_No = models.ForeignKey(Dept, on_delete=models.CASCADE)

    
