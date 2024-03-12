from django.db import models
from main_info.models import MyUser

# These are the models to handle all the data about businesses

"""
the general model to handle the general information about a business
"""
class Business(models.Model):
    owner = models.ForeignKey(MyUser, blank=True, null= True, on_delete= models.SET_NULL)
    name = models.CharField(max_length= 25, blank=False)
    city = models.CharField(max_length= 20, blank= False)
    contact = models.IntegerField(blank = False)
    email = models.TextField(max_length= 35, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

# this model is to handle businesses that sell goods to customers
class Selling_Business(models.Model):
    business_details = models.OneToOneField(Business, blank= False, null= False, on_delete= models.CASCADE)
    category = models.TextField(max_length= 25, blank= False, null = False)
    delivery_options = models.BooleanField(default=True)
    customer = models.ManyToManyField(MyUser, blank=True)

    def __str__(self) -> str:
        return self.business_details.name
    
# this model is to handle businesses that offer a service to the customers
class Service_Business(models.Model):
    business_details = models.OneToOneField(Business, blank= False, null= False, on_delete= models.CASCADE)
    service = models.TextField(max_length= 25, blank= False, null = False)
    appointment_options = models.BooleanField(default=True)
    customer = models.ManyToManyField(MyUser, blank=True)

    def __str__(self) -> str:
        return self.business_details.name
