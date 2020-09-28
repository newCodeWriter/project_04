from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cash_balance = models.FloatField(default=1500)

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

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=8)
    shares = models.IntegerField(default=0)
    date = models.DateField('purchase date')
    paid = models.FloatField()

    def __str__(self):
        return "%s, %d" %  (self.symbol, self.shares)
