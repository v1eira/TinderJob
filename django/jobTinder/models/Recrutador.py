from django.db import models
from .Perfil import Perfil


class Recrutador(Perfil):
    def __init__(self, nome, cpf,telefone ,email, senha, data_nascimento):
        super().__init__(nome, cpf,telefone, email, senha, data_nascimento)

    #def _gerenciarVaga():