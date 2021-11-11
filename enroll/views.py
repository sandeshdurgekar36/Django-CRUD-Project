from django.shortcuts import render,HttpResponseRedirect
from .forms import Student
from .models import User

# Create your views here
# this function is to add item and show all items

###############strats from here##################
def show(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = Student()
    else:
        fm = Student()
    stu = User.objects.all()
    return render(request, 'enroll/forms.html', {'form': fm, 'stud':stu})

def deletedata(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def edit(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            fm = Student()
    else:
        pi = User.objects.get(pk=id)
        fm = Student(instance=pi)
    return render(request, 'enroll/edit.html',{'form': fm, 'id': id})

    
    
    

# ########################################end ##########################
####################################################



#############
############
############















    
