from django.db import models


class Perfil(models.Model):

    nome:str = models.CharField(max_length=50)
    cpf:str = models.CharField(max_length=11)
    telefone = models.CharField(max_length=13)
    email:str = models.EmailField()
    senha:str = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE)


    #Métodos
    def __init__(self, nome, cpf, telefone, email, senha, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.data_nascimento = data_nascimento
        self.endereco = endereco


        #def desfazerMatch():
        #def aceitarMatch():
        #def gerenciarPerfil():

    def __str__(self):
        return self.nome
    class Meta:
        app_label = 'jobTinder'

        c = Candidato("Marcos", "1234", "c@a.com","senhafacil", "18/5/1999", "nenhuma", "todas", "Vitoria")