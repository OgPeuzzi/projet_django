from django.contrib import admin
from .models import Student, Employee

# Register your models here.

class studentAdmin(admin.ModelAdmin):

        list_display = ('first_name', 'last_name', 'contact', 'email', 'age')

admin.site.register(Student)

class EmployeeAdmin(admin.ModelAdmin):

        list_display = ('eid', 'ename', 'econtact')

admin.site.register(Employee)

