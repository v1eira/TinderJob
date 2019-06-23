from django.db import models


class Endereco(models.Model):
    cep: str = models.CharField(max_length=20)
    rua: str = models.CharField(max_length=100)
    complemento: str = models.CharField(max_length=50)
    numero: int = models.IntegerField()
    bairro: str = models.CharField(max_length=50)
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE)

    def __str__(self):
        return self.rua

    class Meta:
        app_label = 'jobTinder'
