from django.db import models
from django.conf import settings

class Exchange(models.Model):
    id = models.AutoField(primary_key=True)
    nameKR = models.CharField(max_length=30, default="")
    nameEN = models.CharField(max_length=30, default="")

class Crypto(models.Model):
    id = models.AutoField(primary_key=True)
    nameKR = models.CharField(max_length=30, default="")
    nameEN = models.CharField(max_length=30, default="")

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exchanges = models.ManyToManyField(Exchange, related_name="exchanges")
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, related_name="crypto", null=True)