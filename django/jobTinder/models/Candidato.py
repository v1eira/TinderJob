from django.db import models
from .Usuario import Usuario


class Candidato(Usuario):
    CPF = models.CharField(max_length=50)
    # experiencia = models.ListField(max_length=60)
    # trabalhosPassados = models.ListField(max_length=60)
    dataNascimento = models.DateField()
    localPreferencia = models.CharField(max_length=50)

    def __init__(self, nome, email, senha, cpf, data_nascimento, local_preferencia):
        super().__init__(nome, email, senha)
        self.CPF = cpf
        self.dataNascimento = data_nascimento
        self.localPreferencia = local_preferencia

    # def criaVaga():
    # def deletaVaga():
    # def atualizaVaga():

    class Meta:
        app_label = 'jobTinder'
