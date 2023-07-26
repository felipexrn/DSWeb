from django.urls import path

from . import views

app_name = 'financas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('busca/', views.BuscaView.as_view(), name='busca'),
    path('balancete/<int:pk>/', views.DetalheView.as_view(), name='detalhe'),
    path('novo_balancete/', views.NovoBalanceteView.as_view(), name='novo_balancete'),
    path('balancete/<int:balancete_id>/lancamento/<int:pk>/', views.LancamentoView.as_view(), name='lancamento'),
    path('balancete/<int:pk>/nova_receita/', views.NovaReceitaView.as_view(), name='nova_receita'),
    path('balancete/<int:pk>/nova_despesa/', views.NovaDespesaView.as_view(), name='nova_despesa'),
    path('balancete/<int:pk>/novo_lancamento/', views.NovoLancamentoView.as_view(), name='novo_lancamento'),
    path('/login', views.LoginView.as_view(), name='login'),
]
