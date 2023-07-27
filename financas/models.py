from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=200, default="")
    class Meta:
        verbose_name_plural = 'Usuarios'
    def __str__(self):
        return self.usuario

class Balancete(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    data = models.DateTimeField('Data do Balancete')
    def __str__(self):
        return self.nome
    def total_receitas(self):
        receitas = 0.0
        for lancamento in self.lancamento_set.filter(despesa="False"):
          receitas += lancamento.valor  
        return receitas
    def total_despesas(self):
        despesas = 0.0
        for lancamento in self.lancamento_set.filter(despesa="True"):
          despesas += lancamento.valor  
        return despesas
    def saldo_total(self):
        return self.total_receitas() - self.total_despesas()
    class Meta:
        verbose_name_plural = 'Balancetes'

class Lancamento(models.Model):
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField(default=0.0)
    foto = models.ImageField(upload_to='media/img/financas/', default='DiagramaDominioFinancas.png')
    despesa = models.BooleanField(default=False)
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name_plural = 'Lançamentos'
