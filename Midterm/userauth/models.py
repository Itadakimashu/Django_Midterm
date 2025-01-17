from django.db import models
from django.contrib.auth.models import User
from car.models import Car

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"{self.user.username} - {self.car.name}"