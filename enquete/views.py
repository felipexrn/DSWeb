from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Felipe Xavier de Carvalho</h1><h1>20221014040007</h1>")

def detail(request, question_id):
    return HttpResponse("Você está olhando para a questão %s." % question_id)

def results(request, question_id):
    response = "Você está olhando para os resultados da questão %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s." % question_id)