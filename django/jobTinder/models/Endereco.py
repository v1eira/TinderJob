from django.db import models


class Endereco(models.Model):
    cep: str = models.CharField(max_length=20)
    rua: str = models.CharField(max_length=100)
    complemento: str = models.CharField(max_length=50)
    numero: int = models.IntegerField()
    bairro: str = models.CharField(max_length= 50)
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE)

    def __init__(self, cep, rua, complemento, numero, bairro, cidade):
        self.cep = cep
        self.rua = rua
        self.complemento = complemento
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade

    class Meta:
        app_label = 'jobTinder'
