from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import View
from .models import *
from django.urls import reverse
import datetime
from django.utils import timezone
from .forms import LancamentoForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        balancetes = Balancete.objects.all()
        context = {'balancetes': balancetes}
        usuario = request.user
        if usuario.username != '':
            context['usuario'] = usuario
        return render(request, 'financas/index.html', context)

class LoginView(View):
    def get(self, request, *args, **kwargs):
        context = {'usuario': request.user}
        return render(request, 'financas/login.html', context)        

class BuscaView(View):
    def post(self, request, *args, **kwargs):
        balancetes_buscados = Balancete.objects.filter(nome__icontains=request.POST['nome'])
        context = {'balancetes_buscados': balancetes_buscados}
        return render(request, 'financas/busca.html', context)

class DetalheView(View):
    def get(self, request, *args, **kwargs):
        balancete = get_object_or_404(Balancete, pk = kwargs['pk'])
        return render(request, 'financas/detalhe.html', {'balancete': balancete})

class LancamentoView(View):
    def get(self, request, *args, **kwargs):
        lancamento = get_object_or_404(Lancamento, pk = kwargs['pk'])
        context = {'lancamento': lancamento}
        return render(request, 'financas/lancamento.html', context)

class NovoBalanceteView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'financas/novo_balancete.html')
    def post(self, request, *args, **kwargs):
        nome = request.POST['nome']
        data = datetime.datetime.now()
        usuario = request.user.id
        balancete = Balancete(nome = nome, data = data, usuario = usuario)
        balancete.save()
        balancetes = Balancete.objects.all()
        context = {'balancetes': balancetes}
        return render(request, 'financas/index.html', context)

class NovaReceitaView(View):
    def get(self, request, *args, **kwargs):
        balancete = get_object_or_404(Balancete, pk = kwargs['pk'])
        context = {'balancete': balancete}
        return render(request, 'financas/nova_receita.html', context)

class NovaDespesaView(View):
    def get(self, request, *args, **kwargs):
        balancete = get_object_or_404(Balancete, pk = kwargs['pk'])
        context = {'balancete': balancete}
        return render(request, 'financas/nova_despesa.html', context)

class NovoLancamentoView(View):
    def post(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(id=request.POST['balancete_id'])
        descricao = request.POST['descricao']
        valor = request.POST['valor']
        foto = request.POST['imagem']
        despesa = request.POST['despesa']# == "True"
        lancamento = Lancamento(balancete = balancete, descricao = descricao, valor = valor, foto = foto, despesa = despesa)
        lancamento.save()
        return HttpResponseRedirect(reverse('financas:detalhe', args=(balancete.id,)))