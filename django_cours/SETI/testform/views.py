from django.http import HttpResponse
from django.shortcuts import redirect, render
from testform.forms import EmpForm, EmployeeForm
from testform.forms import StudentForm

# Create your views here.

def indexForm(request):
    prod = EmpForm()
    return  render(request, "indexForm.html" # Permet de renvoyer ce qui est dans notre html
                    ,{'form': prod})

def testForm(request):
    student = StudentForm()
    return render(request, "testForm.html"
                    ,{'form': student})

def validation(request):
    return HttpResponse("<h1>L'employé a bel et bien été créée</h1>")

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                return redirect('/validation')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "emp-form.html"
                ,{'form': form})
    