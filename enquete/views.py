from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        latest_question_list = Question.objects.order_by('-pub_date')
        context = {'latest_question_list': latest_question_list}
        return render(request, 'enquete/index.html', context)

class DetailView(View):
    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk = kwargs['pk'])
        return render(request, 'enquete/detail.html', {'question': question})

class ResultsView(View):
    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk = kwargs['pk'])
        return render(request, 'enquete/results.html', {'question': question})

class VoteView(View):
    def post(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk = kwargs['pk'])
        try:
            choice_id = request.POST['choice']
            selected_choice = question.choice_set.get(pk=choice_id)
        except (KeyError, Choice.DoesNotExist):
            context = {
                'question': question,
                'error_message': "Você precisa selecionar uma alternativa válida!"
            }
            # Reexibe o formulário de votação da pergunta.
            return render(request, 'enquete/detail.html', context)
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Sempre retorna uma HttpResponseRedirect após lidar corretamente cos dados da postagem.
            # Isso evita que os dados sejam postados duas vezes se um usuário clicar no botão Voltar.
            return HttpResponseRedirect(reverse('enquete:results', args=(question.id,)))
