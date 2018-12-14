from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    orgaos = Orgao.objects.order_by('-nome',)
    secretaria = {}
    result = []
    for each in orgaos:
        if each.nome == 'SECRETARIA DE TECNOLOGIA DA INFORMAÇÃO E DE COMUNICAÇÃO':
            secretaria = each
        else:
            result.append(each)
    return render(request, 'organograma/index.html', context={'orgaos': result, 'secretaria': secretaria },)


def detail(request, orgao_id):
    orgao = get_object_or_404(Orgao, pk=orgao_id)
    return render(request, 'organograma/detail.html', {'orgao': orgao})


def results(request, orgao_id):
    response = "You're looking at the results of orgao %s."
    return HttpResponse(response % orgao_id)


def time(request, orgao_id):
    return HttpResponse("You're voting on orgao %s." % orgao_id)


def projetos(request):
    projetos = Projeto.objects.order_by('nome')
    return render(request, 'organograma/projetos.html', {'projetos': projetos})

def projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    return render(request, 'organograma/projeto.html', {'projeto': projeto})

