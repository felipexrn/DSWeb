from django.urls import path

from . import views

app_name = 'lablivre'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ligado/<str:computador_id>/', views.LigadoView.as_view(), name='ligado'),
    path('set_bats/', views.SetBatsView.as_view(), name='set_bats'),
]