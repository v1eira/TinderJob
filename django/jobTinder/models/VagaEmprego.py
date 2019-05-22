from django.db import models


class VagaEmprego(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()  
    regimeTrabalho = models.CharField(max_length=100)
    data = models.DateField()
    requisitosObrigatorios = models.CharField(max_length=100)
    requisitosDesejaveis = models.CharField(max_length=100)
    qtdVaga = models.IntegerField()
    disponibilidade = models.BooleanField()

    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'

    def __init__(self, nome, descricao, regimeTrabalho, data, requisitosObrigatorios, requisitosDesejaveis, qtdVaga, disponibilidade, empresa):
        self.nome = nome
        self.descricao = descricao
        self.regimeTrabalho = regimeTrabalho
        self.data = data
        self.requisitosObrigatorios = requisitosObrigatorios
        self.requisitosDesejaveis = requisitosDesejaveis
        self.qtdVaga = qtdVaga
        self.disponibilidade = disponibilidade
        self.empresa = empresa