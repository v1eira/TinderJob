from django.db import models
from .Usuario import Usuario


class Recrutador(Usuario):
    
    empresa = models.ForeignKey("Filial", on_delete=models.CASCADE)
    
    def __init__(self, nome, cpf, email, senha, data_nascimento, empresa):
        super().__init__(nome, cpf, email, senha, data_nascimento)
        self.empresa = empresa

    # def criaVaga():
    # def deletaVaga():
    # def atualizaVaga():

    def __str__(self):
        return super.nome
        
    class Meta:
        app_label = 'jobTinder'
