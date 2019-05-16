from django.db import models


class Usuario(models.Model):

    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=13)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'
        abstract = True

    #Métodos
    def __init__(self, nome, cpf, telefone, email, senha, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.data_nascimento = data_nascimento
