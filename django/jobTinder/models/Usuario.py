from django.db import models


class Usuario(models.Model):

    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'

    #Métodos
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

