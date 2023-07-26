from django import forms
from .models import Lancamento

class LancamentoForm(forms.ModelForm): 
    class Meta: 
        model = Lancamento 
        fields = ['balancete', 'descricao', 'valor', 'foto'] 