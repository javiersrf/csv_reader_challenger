import datetime
from django.db import models


class Operation(models.Model):
    operation_id = models.IntegerField(name="operation_id",primary_key=True,serialize=True)
    name =  models.CharField(name="name",max_length=200)
    quantity = models.IntegerField(name="quantity")
    total = models.FloatField(name="total")
    register_date = models.DateTimeField(default=datetime.datetime.now)


class ProviderSell(models.Model):
    provider = models.CharField(name="provider",max_length=100)
    quantity = models.IntegerField(name="quantity")
    total = models.FloatField(name="total")
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    register_date = models.DateTimeField(default=datetime.datetime.now)


class RegisterSell(models.Model):
    buyer = models.CharField(name="buyer",max_length=100)
    quantity = models.IntegerField(name="quantity")
    total = models.FloatField(name="total")
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    register_date = models.DateTimeField(default=datetime.datetime.now)
