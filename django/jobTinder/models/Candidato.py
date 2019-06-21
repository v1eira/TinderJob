from django.db import models
from .Perfil import Perfil


class Candidato(Perfil):
    localPreferencia:str = models.CharField(max_length=50)
    trabalhosPassados: str = models.TextField()
    competencias = models.ForeignKey("Competencias", on_delete=models.CASCADE)

    def __init__(self, nome, cpf, telefone, email, senha, data_nascimento, endereco, trabalhosPassados, competencias, local_preferencia):
        super().__init__(nome, cpf, telefone, email, senha, data_nascimento, endereco)
        self.trabalhosPassados = trabalhosPassados
        self.competencias = competencias
        self.local_preferencia = local_preferencia

    # def pesquisarVaga():

    def __str__(self):
        return super.nome

    def __str__(self):
        return super().__str__()
        
    class Meta:
        app_label = 'jobTinder'