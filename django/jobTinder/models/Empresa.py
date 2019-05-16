from django.db import models
from .Usuario import Usuario


class Empresa(models.Model):
    #CNPJ = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50) #criar tabela Contato?
    descricao = models.CharField(max_length=120)


    class Meta:
        app_label = 'jobTinder'
        #abstract = True

    def __init__(self, nome, email, descricao):
        self.nome = nome
        #self.cnpj = cnpj
        self.email = email
        self.descricao = descricao

    class Meta:
        app_label = 'jobTinder'
