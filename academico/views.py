from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        diarios = Diario.objects.all()
        context = {'diarios': diarios}
        return render(request, 'academico/index.html', context)
    
