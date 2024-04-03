from django.shortcuts import render
from django.http import HttpResponse
from .models import Pergunta
from django.template import loader


def index(request):
    lista = Pergunta.objects.all()
    template = loader.get_template("enquetes/index.html")
    contexto = {
        'lista_enquetes': lista
    }
    return HttpResponse(template.render(contexto, request))
    # return HttpResponse(
    #     "<h1>Disciplina:DSWeb   Período: 2024.1</h1><h2>Matrícula: 20231014040005 - Aluno:Felipe da Costa Ferreira</h2>"
    #     )

def detalhes(request, pergunta_id):
    result = "DETALHES da enquete de número %s"
    return HttpResponse(result % pergunta_id)

def votacao(request, pergunta_id):
    result = "VOTAÇÃO da enquete de número %s"
    return HttpResponse(result % pergunta_id)

def resultado(request, pergunta_id):
    result = "RESULTADO da enquete de número %s"
    return HttpResponse(result % pergunta_id)