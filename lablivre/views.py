from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect, FileResponse
from django.views import View
from .models import Laboratorio, Computador
from django.utils import timezone
import datetime

class IndexView(View):
    def get(self, request, *args, **kwargs):
        laboratorios = Laboratorio.objects.all()
        contexto = {'laboratorios': laboratorios}
        for laboratorio in laboratorios:
            for computador in laboratorio.computador_set.all():
                print(computador.identificador)
                print(computador.ligado)
        return render(request, 'lablivre/index.html', contexto)

class LigadoView(View):
    def get(self, request, *args, **kwargs):
        computador = get_object_or_404(Computador, identificador = kwargs['computador_id'])
        computador.ligado = datetime.datetime.now()
        computador.save()
        return HttpResponseRedirect(reverse('lablivre:index'))

class SetBatsView(View):
    def get(self, request, *args, **kwargs):
        laboratorios = Laboratorio.objects.all()
        contexto = {'laboratorios': laboratorios}
        for laboratorio in laboratorios:
            for computador in laboratorio.computador_set.all():
                arquivo = "lablivre/bats/lablivre_" + laboratorio.nome + "_" + computador.patrimonio + ".bat"
                bat = open(arquivo, "w")
                bat.write("curl " + request.get_host() + "/lablivre/ligado/" + str(computador.identificador) + "/")
                bat.close()
        return HttpResponseRedirect(reverse('lablivre:index'))

# Para uso no dowload dos arquivos de configuração return FileResponse(open("caminho_do_arquivo", "rb"))


        
        