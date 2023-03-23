from django.contrib import admin
from .models import Property, Category, Agent, City, Contact

# Register your models here.

admin.site.register(Property)
admin.site.register(Category)
admin.site.register(Agent)
admin.site.register(City)
admin.site.register(Contact)

# class PropertyAdmin(admin.ModelAdmin):

#     list_display = ('name', 'price', 'Property_type', 'category', 'area', 'beds_number', 'baths_number', 'garages_number', 'image')

# class CategoryAdmin(admin.ModelAdmin):

#     list_display = ('Category_name')

# class AgentAdmin(admin.ModelAdmin):

#     list_display = ('agent_name', 'agent_function', 'agent_image')

# class CityAdmin(admin.ModelAdmin):

#     list_display = ('city_name', 'city_department', 'city_picture')

# class ContactAdmin(admin.ModelAdmin):

#     list_display = ('First_name', 'Last_name', ' Email', 'Message')



