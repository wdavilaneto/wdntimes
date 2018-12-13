from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Orgao


def index(request):
    orgaos = Orgao.objects.order_by('nome')
    template = loader.get_template('organograma/index.html')
    context = {'orgaos': orgaos, }
    return render(request, 'organograma/index.html', context)


def detail(request, orgao_id):
    orgao = get_object_or_404(Orgao, pk=orgao_id)
    return render(request, 'organograma/detail.html', {'orgao': orgao})


def results(request, orgao_id):
    response = "You're looking at the results of orgao %s."
    return HttpResponse(response % orgao_id)


def time(request, orgao_id):
    return HttpResponse("You're voting on orgao %s." % orgao_id)
