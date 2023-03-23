from django.db import models

# Create your models here.

property_type = (
                ('S', "sale"),
                ('R', "rent")
    )

class Property(models.Model):

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField (null = True)
    Property_type = models.CharField(max_length=100, choices = property_type)
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    area = models.DecimalField (decimal_places = 10, max_digits = 40)
    beds_number = models.PositiveIntegerField(null = True)
    baths_number = models.PositiveIntegerField(null = True)
    garages_number = models.PositiveIntegerField(null = True)
    image  = models.ImageField(upload_to = "Property", null = True)

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = 'property'
    #     verbose_name_plural = 'properties'

class Category(models.Model):

    Category_name =  models.CharField(max_length=30)

    def __str__(self):
        return self.Category_name
    
    #class Meta:
    #     verbose_name = 'Category'
    #     verbose_name_plural = 'Categories'

class Agent(models.Model):
    agent_name = models.CharField(max_length=350)
    agent_function = models.CharField(max_length=500)
    agent_image  = models.ImageField(upload_to = "Agent", null = True)

    def __str__(self):
        return self.agent_name

    #class Meta:
    #     verbose_name = 'agent'
    #     verbose_name_plural = 'agents'

class City(models.Model):
    city_name = models.CharField(max_length=350)
    city_department = models.CharField(max_length=350)
    city_picture = models.ImageField(upload_to = "City", null = True)

    def __str__(self):
        return self.city_name

    #class Meta:
    #     verbose_name = 'city'
    #     verbose_name_plural = 'cities'

class Contact(models.Model):
    First_name = models.CharField(max_length=350)
    Last_name = models.CharField(max_length=350)
    Email = models.EmailField(max_length = 200)
    Message = models.TextField(max_length=350)

    def __str__(self):
        return self.First_name

    #class Meta:
    #     verbose_name = 'contact'
    #     verbose_name_plural = 'contacts'


    