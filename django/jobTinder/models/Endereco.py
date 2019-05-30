from django.db import models


class Endereco(models.Model):
    rua: str = models.CharField(max_length=100)
    numero: int = models.IntegerField()
    complemento: str = models.CharField(max_length=50)
    bairro: str = models.CharField(max_length= 50)
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE)

    def __init__(self, rua, numero, complemento, bairro, cidade):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade

    class Meta:
        app_label = 'jobTinder'
