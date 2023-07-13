from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Balancete, Lancamento
from django.urls import reverse

class IndexView(View):
    def get(self, request, *args, **kwargs):
        balancetes = Balancete.objects.all()
        context = {'balancetes': balancetes}
        return render(request, 'financas/index.html', context)

class DetalheView(View):
    def get(self, request, *args, **kwargs):
        balancete = get_object_or_404(Balancete, pk = kwargs['pk'])
        return render(request, 'financas/detalhe.html', {'balancete': balancete})

class BuscaView(View):
    def post(self, request, *args, **kwargs):
        balancetes_buscados = Balancete.objects.filter(nome__icontains=request.POST['nome'])
        context = {'balancetes_buscados': balancetes_buscados}
        return render(request, 'financas/busca.html', context)

