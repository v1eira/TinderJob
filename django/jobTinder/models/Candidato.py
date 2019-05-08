from django.db import models
from .Usuario import Usuario


class Candidato(Usuario):
    experiencia = models.ListField(max_length=280)
    habilidades = models.ListField(max_length=50)
    local_preferencia = models.CharField(max_length=50)

    def __init__(self, nome, cpf, email, senha, data_nascimento, experiencia, habilidades, local_preferencia):
        super().__init__(nome, cpf, email, senha, data_nascimento)
        self.experiencia = experiencia
        self.habilidades = habilidades
        self.local_preferencia = local_preferencia

    # def criaVaga():
    # def deletaVaga():
    # def atualizaVaga():

    class Meta:
        app_label = 'jobTinder'
