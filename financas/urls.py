from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'financas'
urlpatterns = [
    
    # urls balancetes
    path('', views.IndexView.as_view(), name='index'),
    path('busca_balancete/', views.BuscaBalanceteView.as_view(), name='busca_balancete'),
    path('balancete/<int:balancete_id>/', views.DetalheBalanceteView.as_view(), name='detalhe_balancete'),
    path('novo_balancete/', views.NovoBalanceteView.as_view(), name='novo_balancete'),
    path('excluir_balancete/<int:pk>/', views.ExcluirBalanceteView.as_view(), name='excluir_balancete'),
    
    # urls lancamentos
    path('balancete/<int:balancete_id>/lancamento/<int:lancamento_id>/', views.DetalheLancamentoView.as_view(), name='detalhe_lancamento'),
    path('balancete/<int:balancete_id>/busca_lancamento',views.BuscaLancamentoView.as_view(), name='busca_lancamento'),
    path('balancete/<int:balancete_id>/nova_receita/', views.NovaReceitaView.as_view(), name='nova_receita'),
    path('balancete/<int:balancete_id>/nova_despesa/', views.NovaDespesaView.as_view(), name='nova_despesa'),
    path('balancete/<int:balancete_id>/novo_lancamento/', views.NovoLancamentoView.as_view(), name='novo_lancamento'),
    path('balancete/<int:balancete_id>/excluir_lancamento/<int:lancamento_id>/', views.ExcluirLancamentoView.as_view(), name='excluir_lancamento'),

    # urls autenticação
    path('usuario/cadastrar/', views.CadastraUsuarioView.as_view(), name='cadastrar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
