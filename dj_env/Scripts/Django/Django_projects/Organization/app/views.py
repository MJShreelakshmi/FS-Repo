from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_dept(request):
    DNo =  int(input('Enter department Number: '))
    DName = input('Enter department Name: ')
    Loc = input('Enter the location of the department: ')
    try:
        TOD = Dept.objects.get_or_create(Dept_No = DNo, DName = DName, Location = Loc)
    except Exception as e:
        print(e)
    if TOD[1]:
        return HttpResponse(f'A new department {DName} with Id: {DNo} is created')
    else:
        return HttpResponse(f'Department with Id: {DNo} already exists. Use a different Department Id')
    def __str__(self):
        return self.DNo
# UNIQUE constraint failed: app_dept.Dept_No while trying to give the duplicate dept_no
'''1 Sales        New delhi
   2 Development  Bangalore
   3 Testing      Bangalore 
'''

def insert_emp(request):
    Dept_no = int(input('Enter department number: '))
    emp_no = int(input('Enter the employee number: '))
    ename = input('Enter the employee name: ')
    job = input('Enter the employee designation: ')
    sal = int(input('Enter the employee salary: '))
    hire_date = input('Enter the date employee was hired: ')
    comm = input('Enter commission: ')
    if comm:
        comm = int(comm)
    else:
        comm = None
    mgr = input('Enter Manager Id: ')
    if mgr:
        mgr = int(mgr)
        try:
            mgro = Emp.objects.get(Emp_No = mgr)
        except Exception as e:
            print(e)
    else:
        mgro = None
    try:
        Dept_no_obj = Dept.objects.get(Dept_No = Dept_no)
    except Exception as e:
        print(e)
    ETO = Emp.objects.get_or_create(Emp_No = emp_no, EName = ename, Sal = sal, Job = job, Hire_date = hire_date, Mgr = mgro, Comm = comm, Dept_No = Dept_no_obj )
    if ETO[1]:
        return HttpResponse(f'A new employee with given details is added to the database')
    else:
        return HttpResponse(f'An employee with given details already exists in the database')
'''
1 101 Smith      Sales Manager        9K    2020-02-12  5 
2 102 James      Senior Developer     9K    2019-12-09  
1 103 Raj        Sales Executive      6K    2021-07-19  4  101
1 104 Rakesh     Sales Executive      6K    2020-06-25  4  101
3 105 Parker     Testing Engineer     7.5K  2021-02-13 
'''
def display_dept(request):
    LDO = Dept.objects.all()
    d = {'LDO':LDO}
    return render(request, 'display_dept.html', d)

def display_emp(request):
    LEO = Emp.objects.all()
    d = {'LEO':LEO}
    return render(request, 'display_emp.html', d)

def joins_select_related(request):
    # LEDO = Emp.objects.select_related('Dept_No').all()
    # LEDO = Emp.objects.select_related('Dept_No').all().filter(EName__startswith = 'R')
    # LEDO = Emp.objects.select_related('Dept_No').filter(Hire_date__year__gt = '2020')
    # LEDO = Emp.objects.select_related('Dept_No').filter(Mgr__isnull = True)
    # LEDO = Emp.objects.select_related('Dept_No').filter(Mgr__isnull = False)
    # LEDO = Emp.objects.select_related('Dept_No').filter(Comm__isnull = True)
    # LEDO = Emp.objects.select_related('Dept_No').filter(Job__contains = 'Sales', Mgr__isnull = False)
    # LEDO = Emp.objects.select_related('Dept_No').filter(DName  = 'Sales')

    LEDO = Emp.objects.filter(Dept_No_id = 2)
    '''
    In case of a ForeignKey you can specify the field name suffixed with _id. 
    In this case, the value parameter is expected to contain the raw value of the foreign model’s primary key
    '''
    d = {'LEDO':LEDO}
    return render(request, 'joins_select_related.html',d)
