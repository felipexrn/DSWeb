from django.db import models
import datetime
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    senha = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
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
    valor = models.FloatField(default=0.0)
    foto = models.ImageField(upload_to='static/img/financas', default='static/img/financas/DiagramaDominioFinancas.png')
    despesa = models.BooleanField(default=False)
    def __str__(self):
        return self.nome
