from django.db import models
from .Usuario import Usuario


class Empresa(Usuario):
    CNPJ = models.CharField(max_length=50)
    descricao = models.CharField(max_length=60)

    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)

    class Meta:
        app_label = 'jobTinder'
