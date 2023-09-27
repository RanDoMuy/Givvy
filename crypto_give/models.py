from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Transactions(models.Model):
    Address= models.CharField(("Wallet Address"), blank=True, max_length= 50)
    Deposit= models.CharField(("Deposit"), blank=True, max_length= 50)
    Received= models.CharField(("Received"), blank=True, max_length= 50)
    Currency= models.CharField(("Currency"), blank=True, max_length= 50)

    def __str__(self):
        return self.Address
    
class Slot(models.Model):
    slots= models.IntegerField(("Slots Left"), default= 100, validators=[MaxValueValidator(9999999999)])