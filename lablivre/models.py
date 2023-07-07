from django.db import models
import datetime
from django.utils import timezone

class Laboratorio(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Computador(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    mac = models.CharField(max_length=200)
    ligado = models.DateTimeField('ligado')
    desligado = models.DateTimeField('desligado')
    status = models.BooleanField(default=False)
    def atualiza_status(self):
        if ligado > desligado:
            status = True
        else:
            status = False
    def __str__(self):
        return self.mac