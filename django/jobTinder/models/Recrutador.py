from django.db import models
from .Perfil import Perfil
from .VagaEmprego import VagaEmprego


class Recrutador(Perfil):
    filial = models.ForeignKey("Filial", on_delete=models.CASCADE)

    #def criarVaga(vaga: VagaEmprego):

    #def _modificarvaga:

    def __str__(self):
        return self.nome
        
    class Meta:
        app_label = 'jobTinder'
