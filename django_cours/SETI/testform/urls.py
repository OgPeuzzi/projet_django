from django.urls import path
from . import views # Nous avons déclarer le point(.) car nous sommes dans le même emplacement sinon on aurais écris le nom de l'app

urlpatterns = [
    path('test-form/', views.indexForm),
    path('test-form-2/', views.testForm),
    path('emp-form/', views.emp),
    path('validation/', views.validation)
]
