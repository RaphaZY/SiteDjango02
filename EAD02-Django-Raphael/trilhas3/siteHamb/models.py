from django.db import models
from datetime import datetime


# Create your models here.

class Site(models.Model):

    nomeCliente = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    fone = models.CharField(max_length=15)
    endereco = models.TextField()
    email = models.CharField(max_length=100)
    date_create = models.DateTimeField(default=datetime.now, blank =True)
