from django.db import models
import base64
from base64 import b64encode
from django.core.files.base import ContentFile


# Create your models here.

class Orgao(models.Model):
    nome = models.CharField(max_length=300, unique=True)
    texto = models.CharField(max_length=2000, null=True, blank=True)
    responsavel = models.CharField(max_length=300, null=True, blank=True)
    funcao = models.CharField(max_length=300, null=True, blank=True)
    local = models.CharField(max_length=300, null=True, blank=True)
    foto = models.BinaryField(null=True, blank=True)
    telefone = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_foto(self):
        result = base64.encodebytes(bytes(self.foto))
        return result.decode("utf-8")


class Projeto(models.Model):
    nome = models.CharField(max_length=300)
    texto = models.CharField(max_length=300, null=True, blank=True)
    andamento = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    release = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    natureza = models.CharField(max_length=100, null=True, blank=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome


class Time(models.Model):
    nome = models.CharField(max_length=300)
    texto = models.CharField(max_length=2000, null=True, blank=True)
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE)
    projeto_atual = models.ForeignKey(Projeto, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=300)
    time = models.ForeignKey(Time, on_delete=models.SET_NULL, null=True)
    texto = models.CharField(max_length=2000, null=True, blank=True)
    funcao = models.CharField(max_length=300, null=True, blank=True)
    cargo = models.CharField(max_length=2000)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    foto = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_foto(self):
        result = base64.encodebytes(bytes(self.foto))
        return result.decode("utf-8")
