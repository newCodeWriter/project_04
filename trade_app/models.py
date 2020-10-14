from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cash_balance = models.DecimalField(max_digits=8, decimal_places=2, default=1500.00)

    def __str__(self):
        return self.user.username

class Position(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    shares = models.IntegerField(default=0)

    def __str__(self):
        return "%s, %d" %  (self.symbol, self.shares)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=8)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.symbol

class StockOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    symbol = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    action = models.CharField(max_length=5, default='buy')
    quantity = models.IntegerField(default=1)
    order_date = models.DateField(null=True)

    def __str__(self):
        return "%s, %s, %s" %  (self.user.username, self.symbol, self.action)
