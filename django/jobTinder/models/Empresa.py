from django.db import models


class Empresa(models.Model):
    CNPJ = models.CharField(max_length=50)
    descricao = models.CharField(max_length=60)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'
