from django.db import models


class Endereco(models.Model):
    CEP = models.CharField(max_length=20)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)

    class Meta:
        app_label = 'jobTinder'
