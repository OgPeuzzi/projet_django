from django import forms
from testform.models import Student, Employee

class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__" # Permet d'afficher tous les chants qui se trouve dans mon model

class StudentForm(forms.Form):

    first_name = forms.CharField(label = "Entrer votre nom"
                                    ,max_length=50, required = False)
    last_name = forms.CharField(label = "Entrer votre prenom"
                                    ,max_length=50, required = False)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"