from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import View
from .models import *
from django.urls import reverse
import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# view de autenticação
class CadastraUsuarioView(View):
    def post(self, request, *args, **kwargs):
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)
        if usuario and senha:
            user = User.objects.create_user(username=usuario, password=senha)
            Usuario.objects.create(usuario=usuario, user=user)
            login(request, user)
        return HttpResponseRedirect(reverse('financas:index'))

class NovoUsuarioView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'financas/novo_usuario.html')

# views do balancete
@method_decorator(login_required, name='dispatch')
class IndexView(View):
    def get(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(user=request.user.id)
        balancetes = Balancete.objects.filter(usuario=usuario).order_by('-data')
        context = {'balancetes': balancetes}
        return render(request, 'financas/index.html', context)      

@method_decorator(login_required, name='dispatch')
class BuscaBalanceteView(View):
    def post(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(user=request.user.id)
        balancetes_buscados = Balancete.objects.filter(usuario=usuario, nome__icontains=request.POST['nome']).order_by('-data')
        context = {'balancetes': balancetes_buscados}
        return render(request, 'financas/index.html', context)

@method_decorator(login_required, name='dispatch')
class DetalheBalanceteView(View):
    def get(self, request, *args, **kwargs):
        balancete = get_object_or_404(Balancete, pk = kwargs['balancete_id'])
        lancamentos = balancete.lancamento_set.all()
        context = {'balancete':balancete, 'lancamentos':lancamentos}
        return render(request, 'financas/detalhe_balancete.html', context)

@method_decorator(login_required, name='dispatch')
class NovoBalanceteView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'financas/novo_balancete.html')
    def post(self, request, *args, **kwargs):
        nome = request.POST['nome']
        data = datetime.datetime.now()
        usuario = Usuario.objects.get(user=request.user.id)
        balancete = Balancete(nome = nome, data = data, usuario = usuario)
        balancete.save()
        return HttpResponseRedirect(reverse('financas:index'))

@method_decorator(login_required, name='dispatch')
class ExcluirBalanceteView(View): 
    def get(self, request, *args, **kwargs):
        balancete = get_object_or_404(Balancete, pk = kwargs['balancete_id'])
        balancete.delete()
        return HttpResponseRedirect(reverse('financas:index'))

# views do lancamento
@method_decorator(login_required, name='dispatch')
class BuscaLancamentoView(View):
    def post(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(user=request.user.id)
        balancete = get_object_or_404(Balancete, pk = kwargs['balancete_id'])
        lancamentos_buscados = Lancamento.objects.filter(balancete=balancete, descricao__icontains=request.POST['descricao'])
        context = {'balancete':balancete,'lancamentos': lancamentos_buscados}
        return render(request, 'financas/detalhe_balancete.html', context)

@method_decorator(login_required, name='dispatch')
class DetalheLancamentoView(View):
    def get(self, request, *args, **kwargs):
        lancamento = get_object_or_404(Lancamento, pk = kwargs['lancamento_id'])
        media_url = settings.MEDIA_URL
        context = {'lancamento': lancamento, 'media_url':media_url}
        return render(request, 'financas/detalhe_lancamento.html', context)

@method_decorator(login_required, name='dispatch')
class NovaReceitaView(View):
    def get(self, request, *args, **kwargs):
        balancete = get_object_or_404(Balancete, pk = kwargs['balancete_id'])
        context = {'balancete': balancete}
        return render(request, 'financas/nova_receita.html', context)

@method_decorator(login_required, name='dispatch')
class NovaDespesaView(View):
    def get(self, request, *args, **kwargs):
        balancete = get_object_or_404(Balancete, pk = kwargs['balancete_id'])
        context = {'balancete': balancete}
        return render(request, 'financas/nova_despesa.html', context)

@method_decorator(login_required, name='dispatch')
class NovoLancamentoView(View):
    def post(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(id=request.POST['balancete_id'])
        descricao = request.POST['descricao']
        valor = request.POST['valor']
        foto = request.FILES['imagem']
        despesa = request.POST['despesa'] # == "True"
        lancamento = Lancamento(balancete = balancete, descricao = descricao, valor = valor, foto = foto, despesa = despesa)
        lancamento.save()
        return HttpResponseRedirect(reverse('financas:detalhe_balancete', args=(balancete.id,)))

@method_decorator(login_required, name='dispatch')
class ExcluirLancamentoView(View): 
    def get(self, request, *args, **kwargs):
        balancete = get_object_or_404(Balancete, pk = kwargs['balancete_id'])
        lancamento = get_object_or_404(Lancamento, pk = kwargs['lancamento_id'])
        lancamento.delete()
        return HttpResponseRedirect(reverse('financas:detalhe_balancete', args=(balancete.id,)))