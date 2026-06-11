from django.db import models

# Create your models here.
class Food_Details(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    size=models.CharField(max_length=100)
    available=models.BigIntegerField()
    price=models.BigIntegerField()
    image=models.FileField()

class category(models.Model):
    category=models.CharField(max_length=100)
    image=models.FileField()

from django.contrib.auth.models import User

# Create your models here.
class user_management_table(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    qualification=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    LOGIN = models.ForeignKey(User, on_delete=models.CASCADE)



class Food_Booking(models.Model):
    USER=models.ForeignKey(user_management_table,on_delete=models.CASCADE)
    FOOD=models.ForeignKey(Food_Details,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=100)
    building_no = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    shipping_address = models.CharField(max_length=100)

