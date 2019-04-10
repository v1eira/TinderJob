import django.db


class Usuario(django.db.models.Model):

    nome = django.db.models.CharField(max_length=50)
    email = django.db.models.CharField(max_length=50)
    senha = django.db.models.CharField(max_length=20)
    endereco = django.db.models.ForeignKey("Endereco")

    #Métodos
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

