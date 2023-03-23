from django import forms
from Property.models import Property, Category, Agent, Contact, City

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__" # Permet d'afficher tous les chants qui se trouve dans mon model

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = "__all__"

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"