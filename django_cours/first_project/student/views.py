from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def helloword(request):
    return HttpResponse("<h2>Hello, Welcome to django!</h2>")

