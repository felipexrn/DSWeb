from django.db import models
from django.utils import timezone
import datetime
import uuid

class Laboratorio(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome
    def get_desligados(self):
        desligados = 0
        for comp in self.computador_set.all():
            if comp.desligado():
                desligados+=1
        return desligados
    class Meta:
        verbose_name_plural = 'Laboratórios'

class Computador(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    identificador = models.UUIDField(default=uuid.uuid4, editable=False)
    patrimonio = models.CharField(max_length=200)
    ligado = models.DateTimeField('ligado', default=timezone.now, editable=False)
    def __str__(self):
        return self.patrimonio
    def desligado(self):
        return self.ligado < (datetime.datetime.now() - datetime.timedelta(minutes=1))
    class Meta:
        verbose_name_plural = 'Computadores'