from django.db import models


class Usuario(models.Model):

    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    #email = models.EmailField() criar tabela Contato? (add telefone)
    senha = models.CharField(max_length=20)
    #data_nascimento = models.DateField() criar tabela para Data
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'
        abstract = True

    #Métodos
    def __init__(self, nome, cpf, email, senha):
        self.nome = nome
        self.cpf = cpf
        #self.email = email
        self.senha = senha
        #self.data_nascimento = data_nascimento
