from django.db import models


class VagaEmprego(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()  #
    regimeTrabalho = models.CharField(max_length=100)
    dataPublicacao = models.DateField()
    requisitos = models.CharField(max_length=100)
    qtdVaga = models.IntegerField()
    disponibilidade = models.BooleanField()

    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'

