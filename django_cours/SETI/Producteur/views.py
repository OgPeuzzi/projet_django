from django.shortcuts import render
import datetime # datetime c'est une biblithéque de python trés reconnue
from django.http import HttpResponse, HttpResponseNotFound # HttpResponse, c'est ce qui nous permet d'avoir le résultat
from django.template import loader
from django.views.decorators.http import require_http_methods

# Create your views here.

def index(request):
    now = datetime.datetime.now() # Permet de renvoyer la date et l'heure actuel par défault
    result = "<html><body><h2>Il est %s !</h2></body></html>"%now # C'est le résultat qu'on doit afficher
    return HttpResponse(result) # %s c'est l'affichage et le %now, c'est la déclaration

def show(request):
    a = 4
    b = 7
    c = a + b
    if c == 12:
        html = "<html><body><h2>Le résultat est : %s !</h2></body></html>"%c
        return HttpResponse(html)
    elif c < 12:
        html = "<html><body><h2>Le résultat est : %s !</h2></body></html>"%c
        return HttpResponse(html)
    else:
        html = "<html><body><h2>Le résultat est : %s !</h2></body></html>"%c
        return HttpResponse(html)

def home(request):
    return HttpResponse("<h2>Ok!!!</h2>")

def account(request):
    return HttpResponse("<h2>Bonsoir!!!</h2>")

def welcome(request):
    loader
    template = loader.get_template('index.html') # Permet de charger les templates
    name = {
        'student': 'Kurt Russell',
        'parent': 'Ferdinand',
    }
    return HttpResponse(template.render(name))

def testing(request):

    @require_http_methods(["GET"])
    def hello(request):
        return HttpResponse('<h1>This is Http GET request</h1>')

def new(request):
    loader
    template = loader.get_template('new.html') 

    return HttpResponse(template.render())





# Views C'est le fichier par défault pour déclarer nos views.