from django.db import models
from main_info.models import MyUser
from prods_servs.models import Product, Service

"""
    this is the model to handle all models related to communication ie messages, appointments, orders
"""

class Messages(models.Model):
    sender = models.ForeignKey(MyUser, blank=False, on_delete = models.CASCADE)
    receiver = models.ForeignKey(MyUser, blank=False, on_delete= models.CASCADE, related_name="message_reciever")
    message = models.TextField(max_length= 150, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.message
    
class Order(models.Model):
    customer = models.ForeignKey(MyUser, blank=False, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE)
    time_of_placement = models.DateTimeField(auto_now_add=True)
    number_of_items = models.IntegerField(blank=False, default=1)

class Appointment(models.Model):
    customer = models.ForeignKey(MyUser, blank=False, on_delete=models.CASCADE)
    service_booked = models.ForeignKey(Service, blank=False, on_delete=models.CASCADE)
    time_of_appointment = models.DateTimeField()