from django.db import models


class Competencias(models.Model):
    nome: str = models.CharField(max_length=100)
    nivel: float = models.FloatField()
    areaConhecimento: str = models.CharField(max_length=50)
    descricao: str = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
        
    class Meta:
        app_label = 'jobTinder'
