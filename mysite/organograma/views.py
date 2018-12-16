from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import *
import gitlab


def index(request):
    orgaos = Orgao.objects.order_by('-nome', )
    secretaria = {}
    result = []
    for each in orgaos:
        if each.nome == 'SECRETARIA DE TECNOLOGIA DA INFORMAÇÃO E DE COMUNICAÇÃO':
            secretaria = each
        else:
            result.append(each)

    return render(request, 'organograma/index.html', context={'orgaos': result, 'secretaria': secretaria}, )


def times(request, orgao_id):
    orgao = get_object_or_404(Orgao, pk=orgao_id)
    return render(request, 'organograma/times.html', {'orgao': orgao})


def time(request, orgao_id):
    return HttpResponse("You're voting on orgao %s." % orgao_id)


def results(request, orgao_id):
    response = "You're looking at the results of orgao %s."
    return HttpResponse(response % orgao_id)


def projetos(request):
    projetos = Projeto.objects.order_by('nome')
    return render(request, 'organograma/projetos.html', {'projetos': projetos})


def projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    gl_project = {}
    events = []
    if projeto.gitlab_id:
        URL = 'https://gitlab.mprj.mp.br'
        gl = gitlab.Gitlab(URL, private_token='GyxKCZbYBpRXze55RyAz', ssl_verify=False, per_page=100)
        gl_project = gl.projects.get(projeto.gitlab_id)
        events = gl_project.events.list()

    return render(request, 'organograma/projeto.html', {'projeto': projeto, 'gl_project': gl_project, 'events': events})


def artigos(request):
    # projetos = Projeto.objects.order_by('nome')
    return render(request, 'organograma/artigos.html', {})


def artigo(request, artigo_id=0):
    # projetos = Projeto.objects.order_by('nome')
    return render(request, 'organograma/artigo.html', {})


def demandas(request):
    # projetos = Projeto.objects.order_by('nome')
    return render(request, 'organograma/demandas.html', {})


def demanda(request, demanda_id=0):
    # projetos = Projeto.objects.order_by('nome')
    return render(request, 'organograma/artigo.html', {})


def perfil(request, perfil_id):
    pessoa = get_object_or_404(Pessoa, pk=perfil_id)
    return render(request, 'organograma/perfil.html', {'pessoa': pessoa})


def agil(request):
    # projetos = Projeto.objects.order_by('nome')
    return render(request, 'organograma/agil.html', {})


def dashboard(request):
    # projetos = Projeto.objects.order_by('nome')
    return render(request, 'organograma/dashboard.html', {})
