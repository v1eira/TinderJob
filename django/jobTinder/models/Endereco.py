from django.db import models


class Endereco(models.Model):
    rua: str = models.CharField(max_length=100)
    numero: int = models.IntegerField()
    complemento: str = models.CharField(max_length=50)
    bairro: str = models.CharField(max_lenght= 50)

    class Meta:
        app_label = 'jobTinder'
