from django.db import models


# Create your models here.

class Orgao(models.Model):
    nome = models.CharField(max_length=300, unique=True)
    texto = models.CharField(max_length=2000, blank=True)
    responsavel = models.CharField(max_length=300, blank=True)
    funcao = models.CharField(max_length=300, blank=True)
    foto = models.BinaryField(blank=True)

    def __str__(self):
        return self.nome


class Time(models.Model):
    nome = models.CharField(max_length=300)
    texto = models.CharField(max_length=2000, blank=True)
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=300)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=300)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, blank=True, null=True)
    texto = models.CharField(max_length=2000, blank=True)
    funcao = models.CharField(max_length=300, blank=True)
    cargo = models.CharField(max_length=2000)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    foto = models.BinaryField(blank=True)

    def __str__(self):
        return self.nome
