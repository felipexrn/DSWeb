from django.shortcuts import render
from django.views import View
from .models import Laboratorio, Computador

class IndexView(View):
    def get(self, request, *args, **kwargs):
        laboratorios = Laboratorio.objects.all()
        computadores = Computador.objects.all()
        for pc in computadores:
            lig = pc.ligado
            desl = pc.desligado
            if (lig < desl):
                pc.status = False
            else:
                pc.status = True
            pc.save()
        desligados = Computador.objects.filter(status = False)
        contexto = {'laboratorios': laboratorios,'desligados': desligados}
        return render(request, 'lablivre/index.html', contexto)
        