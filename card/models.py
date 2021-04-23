from django.db import models
from django.conf import settings

class Exchange(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Crypto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exchange1 = models.ForeignKey(Exchange, on_delete=models.SET_NULL, null=True, related_name="exchange1")
    exchange2 = models.ForeignKey(Exchange, on_delete=models.SET_NULL, null=True, related_name="exchange2")
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, related_name="crypto")