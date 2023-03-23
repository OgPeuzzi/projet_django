"""SETI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Producteur import views

urlpatterns = [
    path('admin/', admin.site.urls), # C'est le chemain par défault de notre application
    path('index/', views.index), # C'est pour aller dans views et prendre l'index et l'affiche dans notre navigateur
    path('show/', views.show),
    path('home/', views.home),
    path('account/', views.account),
    path('welcome/', views.welcome),
    path('testing/', views.testing),
    path('new/', views.new),
    path('', include('testform.urls')),
]
# L'url c'est une chemain par lequel on affiche nos views