from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from Property.forms import ContactForm
from django.shortcuts import redirect, render
from .models import *
from django.core.mail import send_mail

# Create your views here.

#def indexForm(request):
 #   prod = PropertyForm()
  #  return  render(request, "index.html" # Permet de renvoyer ce qui est dans notre html
   #                 ,{'form': prod})

#def categoryForm(request):
 #   category = CategoryForm()
  #  return render(request, "category.html"
   #                 ,{'form': category})

#def agentForm(request):
 #   agent = AgentForm()
  #  return render(request, "agent.html"
   #                 ,{'form': agent})

#def cityForm(request):
 #   city = CityForm()
  #  return render(request, "city.html"
   #                 ,{'form': city})
from django.template import loader

# def index(request):
#     loader
#     template = loader.get_template('index.html') 

#     return HttpResponse(template.render())

def about(request):
    loader
    template = loader.get_template('about.html') 

    return HttpResponse(template.render())

# def about(request):
#     agents_list = Agent.objects.all()
#     context = {'agents': agents_list}
#     return render(request, 'agent.html', context)

#def contact(request):
 #   loader
  #  template = loader.get_template('contact.html') 

   # return HttpResponse(template.render())

# def agent(request):
#     loader
#     template = loader.get_template('agent.html') 

#     return HttpResponse(template.render())

def agent(request):
    agents_list = Agent.objects.all()
    context = {'agents': agents_list}
    return render(request, 'agent.html', context) 

def properties(request):
    Properties_list = Property.objects.all()
    context = {'property_list': Properties_list}
    return render(request, 'property.html', context)

def index(request):
    city_list = City.objects.all()
    agent = Agent.objects.all()
    Properties_list = Property.objects.all()
    context = {'agents': agent, 'property_list': Properties_list, 'city': city_list}
    return render(request, 'index.html', context) 

# def properties(request):
#     loader
#     template = loader.get_template('property.html') 

#     return HttpResponse(template.render())

def contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            name = contact.cleaned_data['First_name']
            surname = contact.cleaned_data['Last_name']
            object = "Monsieur " + name + ' ' + surname
            msg = contact.cleaned_data['Message']
            Envoyé_à = contact.cleaned_data['Email']
            res = send_mail(object,msg,settings.EMAIL_HOST_USER,[Envoyé_à])
            if (res == 1):
            #contact.save()
                try:
                    msg = "Mail sent successfuly"
                    return redirect('/')
                except:
                    pass
            else:
                msg = "Mail could not sent"
                print(msg)
            return redirect('/')

    else:
        contact = ContactForm()
    return render(request, "contact.html"
                ,{'form': contact})


def mail(request):
    object = "Salut"
    msg = "Félicitation"
    Envoyé_à = "b.diagne3@isepdiamniadio.edu.sn"
    res = send_mail(object,msg,settings.EMAIL_HOST_USER,[Envoyé_à])
    if (res == 1):
        msg = "Mail sent successfuly"
    else:
        msg = "Mail could not sent"
        print(msg)
    return HttpResponse(msg)
