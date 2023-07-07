from django.shortcuts import render
from django.views import View
from .models import Laboratorio

class IndexView(View):
    def get(self, request, *args, **kwargs):
        laboratorios = Laboratorio.objects.all()
        contexto = {'laboratorios': laboratorios}
        return render(request, 'lablivre/index.html', contexto)