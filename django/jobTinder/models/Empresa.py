from django.db import models
from .Usuario import Usuario


class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    descricao = models.CharField(max_length=120)


    class Meta:
        app_label = 'jobTinder'
        #abstract = True

    def __init__(self, nome, cnpj, email, descricao):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.descricao = descricao

    class Meta:
        app_label = 'jobTinder'
