from django.shortcuts import render
from django.views import View
from .models import Laboratorio, Computador
import datetime

class IndexView(View):
    def get(self, request, *args, **kwargs):
        laboratorios = Laboratorio.objects.all()
        desligados = Computador.objects.filter(ligado__lt = datetime.datetime.now() - datetime.timedelta(minutes=1))
        contexto = {'laboratorios': laboratorios,'desligados': desligados}
        return render(request, 'lablivre/index.html', contexto)


        
        