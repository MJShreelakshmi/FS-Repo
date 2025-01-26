from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q, Prefetch, Max, Min, Count, Avg, Sum
from datetime import date

# Create your views here.
def insert_dept_fe(request):
    if request.method == 'POST':
        DNo =  request.POST['Dept_No']
        DName =  request.POST['DName']
        Loc =  request.POST['Location']
        try:
            TOD = Dept.objects.get_or_create(Dept_No = DNo, DName = DName, Location = Loc)
            if TOD[1]:
                return HttpResponse(f'A new department object {DName} with Id {DNo} with is created')
            else:
                return HttpResponse(f'Department : {DNo} {DName} at {Loc} already exists')
        except Exception as e:
            return HttpResponse(e)
    return render(request, 'insert_dept_fe.html')


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

def insert_emp_fe(request):
    LEO = Emp.objects.all()
    de = {'LEO':LEO}
    LDO = Dept.objects.all()
    dd = {'LDO':LDO}
    d1 = {'LDEO': de|dd }
    '''
        Rendering multiple dicts
    d1---> {'LDEO':{'LEO':Queryset[...], 'LDO':{'LDO':Queryset[...]}  }
    Accessing in FE:- LDEO.LEO.attr_val or LDEO.LDO.attr_val
                OR 
    '''
    d = {'LEO':de, 'LDO':dd}
    '''
    d---> {'LEO':{'LEO':Queryset[...]}, 'LDO':{'LDO':Queryset[...]}  }
    Accessing in FE:- LEO.LEO.attr_val or LDO.LDO.attr_val
    '''
    if request.method == 'POST':
        Emp_No = request.POST['Emp_No']
        EName = request.POST['EName']
        Job = request.POST['Job']
        Mgr = request.POST['Mgr']
        try:
            dat = request.POST['Hire_date'].split('-')
            Hire_date =  date(day = dat[0], month=dat[1], year=dat[2])
        except:
            Hire_date = None
        Sal = float(request.POST['Sal'])  
        try:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            Comm = float(request.POST['Comm'])
        except:
            Comm = None
        Dept_No = request.POST['Dept_No']
        do = Dept.objects.get(Dept_No = Dept_No)
        mo = Emp.objects.get(Emp_No = Mgr)
        print(Sal, type(Sal))
        try:
            TEO = Emp.objects.get_or_create(Emp_No = Emp_No, EName = EName, Job = Job, Mgr = mo, Hire_date = Hire_date, Sal = Sal, Comm = Comm, Dept_No = do)
            if TEO[1]:
                return HttpResponse(f'An emp object with Emp_No {Emp_No} is created')
            else:
                return HttpResponse(f'Emp object with Emp_No {Emp_No} is created')
        except Exception as e:
                return HttpResponse(e)
    return render (request, 'insert_emp_fe.html',d)

def display_dept(request):
    LDO = Dept.objects.all()
    d = {'LDO':LDO}
    return render(request, 'display_dept.html', d)

def display_emp(request):
    LEO = Emp.objects.all()
    d = {'LEO':LEO}
    return render(request, 'display_emp.html', d)

def dql_dept(request):
    LDO = Dept.objects.all()
    # all dept names
    LDO = Dept.objects.values_list('DName')
    #  all dname and locations
    LDO = Dept.objects.values('DName', 'Location')
    # 
    # LDO =
    print(LDO)
    d = {'LDO':LDO}
    return render(request, 'display_dept.html',d)

def dql_emp(request):
    LEO = Emp.objects.all()
    LEO = Emp.objects.values( 'EName', 'Hire_date')
    LEO = Emp.objects.annotate(E = Length('EName')) # not working
    d = {'LEO':LEO}
    return render(request, 'display_emp.html', d )

