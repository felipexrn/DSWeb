from django.db import models
from django.utils import timezone

class Laboratorio(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Computador(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    patrimonio = models.CharField(max_length=200)
    ligado = models.DateTimeField('ligado')
    def __str__(self):
        return self.patrimonio

class Mac(models.Model):
    computador = models.ForeignKey(Computador, on_delete=models.CASCADE)
    mac = models.CharField(max_length=200)
    def __str__(self):
        return self.mac