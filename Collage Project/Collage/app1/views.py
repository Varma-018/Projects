from django.shortcuts import render,redirect

from app1.models import Department,HOD,Professor,Students

from app1.forms import Department_Registration,HOD_Registration,Professor_Registration,Student_Registration 

def home(request):
    return render(request, 'home.html')


######################################################



#################################################################

def department(request):
    if request.method == "GET":
        search = request.GET.get('search',None)
        if search:
            data = Department.objects.filter(name__startswith=search)|Department.objects.filter(code__startswith = search)
        else:
            data = Department.objects.all()

    if request.method == "POST":
        fm = Department_Registration(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('department')
        else:
            data = Department.objects.all()

    else:
         fm = Department_Registration()
    context = {
        'data':data,
        'fm':fm,
    }
    return render(request, "Dept.html",context)

            #######################
def dele_Dept(request,pk):
    if request.method == "POST":
        pi = Department.objects.get(id=pk)
        pi.delete()
        return redirect('department')
    
    #############################

def update_Dept(request,pk):
    pi = Department.objects.get(id = pk)
    fm = Department_Registration(instance=pi)
    if request.method == "POST":
        pi = Department.objects.get(id=pk)
        fm = Department_Registration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('department')
 
   
    data = Department.objects.all()
    context = {
        'data':data,
        'updateForm':fm,
    }
    
    return render(request,'Dept.html',context)



#########################################################################################################

def hod(request):
    if request.method == "GET":
        serach = request.GET.get('search',None)
        if serach:
            data = HOD.objects.filter(name__startswith = serach)|HOD.objects.filter(Department__name__startswith = serach)|HOD.objects.filter(phone__startswith = serach)
        else:
            data = HOD.objects.all()

    if request.method =="POST":
        fm = HOD_Registration(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('hod')
        else:
            data = HOD.objects.all()
    else:
        fm = HOD_Registration()
    context = {
        'data':data,
        'fm':fm
    }
    return render(request, 'Hod.html',context)

def delete_Hod(request,pk):
    if request.method =="POST":
        pi = HOD.objects.get(id=pk)
        pi.delete()
        return redirect('hod')
    
def update_Hod(request,pk):
    pi = HOD.objects.get(id=pk)
    fm = HOD_Registration(instance=pi)
    if request.method =="POST":
        pi = HOD.objects.get(id=pk)
        fm = HOD_Registration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect ('hod')
    data = HOD.objects.all()
    context = {
        'data':data,
        'updateForm':fm
    }

    return render(request, 'Hod.html',context)

###########################################################################################################

def professor(request):
    if request.method == "GET":
        search = request.GET.get('search',None)
        if search:
            data = Professor.objects.filter(name__startswith = search)|Professor.objects.filter(Department__name__startswith = search)|Professor.objects.filter(phone__startswith = search)|Professor.objects.filter(Subject__startswith = search)
        else:
            data = Professor.objects.all()
    if request.method =="POST":
        fm = Professor_Registration(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('professor')
        else:
            data = Professor.objects.all()

    else:
        fm = Professor_Registration()

    context = {
        'data':data,
        'fm':fm

    }
    return render (request, "Proff.html",context)

def delete_professor(request,pk):
    if request.method == "POST":
        pi = Professor.objects.get(id=pk)
        pi.delete()
        return redirect('professor')
    
def update_professor(request,pk):
    pi = Professor.objects.get(id=pk)
    fm  = Professor_Registration(instance=pi)
    if request.method == "POST":
        pi = Professor.objects.get(id=pk)
        fm  = Professor_Registration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('professor')
    data = Professor.objects.all()

    context = {
        'data':data,
        'updateForm':fm

    }
    return render (request, "Proff.html",context)


#################################################################################################

def student(request):
    if request.method == "GET":
        search = request.GET.get('search',None)
        if search:
            data = Students.objects.filter(name__startswith = search)|Students.objects.filter(name__startswith = search)|Students.objects.filter(Department__name__startswith = search)|Students.objects.filter(Register_ID__startswith = search)
        else:
            data = Students.objects.all()
    if request.method =="POST":
        fm = Student_Registration(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('student')
        else:
            data = Students.objects.all()
    else:
        fm = Student_Registration()

    context = {
        'data': data,
        'fm':fm
    }
    return render(request,'Stud.html',context)

        ##############
def delete_Stud(request,pk):
    if request.method == "POST":
        pi = Students.objects.get(id= pk)
        pi.delete()
        return redirect('student')
    
def update_student(request,pk):
    pi = Students.objects.get(id=pk)
    fm  = Student_Registration(instance=pi)
    if request.method == "POST":
        pi = Students.objects.get(id=pk)
        fm  = Student_Registration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('student')
    data = Students.objects.all()

    context = {
        'data':data,
        'updateForm':fm

    }
    return render (request, "Stud.html",context)



###########################################################################


def search(request):
    if request.method == "GET":

        search = Department.objects.get('search',None)

        if search:
            Department.objects.filter(name__startswith=search)
        else:
            data = Department.objects.all


