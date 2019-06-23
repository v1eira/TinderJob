from django.db import models


class Pais(models.Model):
    nome: str = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'jobTinder'

