from django.db import models

# Create your models here.
from django.db import models
from users.models import User
# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = "service"

class Payment_user(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
    paymentDate = models.DateField(auto_now_add=False)
    expirationDate = models.DateField(auto_now_add=False)
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    service = models.ForeignKey(Services, on_delete =models.CASCADE)
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = "payment_user"

class Expired_payments(models.Model):
    penalty_fee_amount = models.DecimalField(max_digits=9, decimal_places=2, default=40.0)
    payment_user = models.ForeignKey(Payment_user, on_delete =models.CASCADE)
     
    class Meta:
        db_table = "expired_payments"

""" class User(models.Model):
    email = models.CharField(max_length=80, unique=True, default="no@email.com")
    username = models.CharField(max_length=45)
    class Meta:
        db_table = "user" """
        
        