from django.urls import path
from . import views # Nous avons déclarer le point(.) car nous sommes dans le même emplacement sinon on aurais écris le nom de l'app

urlpatterns = [
   path('index/', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('agent/', views.agent, name = 'agent'),
    path('properties/', views.properties, name = 'properties'),
    path('mail/', views.mail),
]
