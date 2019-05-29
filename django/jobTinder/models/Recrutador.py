from django.db import models
from .Perfil import Perfil


class Recrutador(Perfil):
    filial = models.ForeignKey("Filial", on_delete=models.CASCADE)

    def __init__(self, nome, cpf, telefone, email, senha, data_nascimento, endereco,filial):
        super().__init__(nome, cpf, telefone, email, senha, data_nascimento, endereco)
        self.filial = filial

    #def _gerenciarVaga():


    def __str__(self):
        return super().__str__()
        
    class Meta:
        app_label = 'jobTinder'
