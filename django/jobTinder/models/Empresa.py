from django.db import models
from .Usuario import Usuario


class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    descricao = models.CharField(max_length=120)

    def __init__(self, nome, cnpj, email, descricao):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.descricao = descricao

    def __str__(self):
        return self.nome
    
    class Meta:
        app_label = 'jobTinder'
