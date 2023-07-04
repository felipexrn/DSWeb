from django.db import models
import datetime
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    senha = models.CharField(min_length=8)
    status = models.BooleanField
    def __str__(self):
        return self.nome

class Balancete(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    data = models.DateTimeField('Data do Balancete')
    def __str__(self):
        return self.nome

class Lancamento(models.Model):
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField
    foto = models.ImageField
    despesa = models.BooleanField
    def __str__(self):
        return self.nome
