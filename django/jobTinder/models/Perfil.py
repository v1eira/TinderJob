from django.db import models


class Perfil(models.Model):

    nome: str = models.CharField(max_length=50)
    cpf: str = models.CharField(max_length=11)
    telefone: str = models.CharField(max_length=13)
    email: str = models.EmailField()
    senha: str = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE)

    # def desfazerMatch():
    # def aceitarMatch():
    # def gerenciarPerfil():

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'jobTinder'
        abstract = True
