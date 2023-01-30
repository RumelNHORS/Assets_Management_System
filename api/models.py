from django.db import models
from datetime import date
from django.contrib.auth.models import User

#Model For Company
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
#This is the choice of an asset to use some of model's
ASSETS_CHOICES = (
        ('Phone', 'Phones'),
        ('Tablet', 'Tablets'),
        ('Laptop', 'Laptops'),  
    )

class AssetsModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    asset = models.CharField(max_length=10, choices=ASSETS_CHOICES)
    brand = models.CharField(max_length=20)
    quantity = models.IntegerField()
    date = models.DateField(("Date"), default=date.today)
    
    def __str__(self):
        return self.employee_name
    
class CheckIn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    asset = models.CharField(max_length=10, choices=ASSETS_CHOICES)
    checkin_date = models.DateTimeField()
    
    def __str__(self):
        return self.employee_name
    
class CheckOut(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    asset = models.CharField(max_length=10, choices=ASSETS_CHOICES)
    checkout_date = models.DateTimeField()
    
    def __str__(self):
        return self.employee_name
    
class CheckOutAndReturn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    asset = models.CharField(max_length=10, choices=ASSETS_CHOICES)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField()
    
    def __str__(self):
        return self.employee_name

class DeviceLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DEVICE_CHOICE = (
        ('Phone', 'Phones'),
        ('Tablet', 'Tablets'),
        ('Laptop', 'Laptops'), 
    )
    devcice = models.CharField(max_length=10, choices=DEVICE_CHOICE)
    Company_name = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50)
    hand_out_condition = models.CharField(max_length=5000)
    return_condition = models.CharField(max_length=5000)
    
    def __str__(self):
        return self.Company_name
