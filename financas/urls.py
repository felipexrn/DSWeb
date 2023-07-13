from django.urls import path

from . import views

app_name = 'financas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetalheView.as_view(), name='detalhe'),
    path('busca/', views.BuscaView.as_view(), name='busca'),
]